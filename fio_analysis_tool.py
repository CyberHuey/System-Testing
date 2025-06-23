import subprocess
import json
import datetime
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

LOG_FILE = "fio_summary_log.txt"

def run_fio(config, output):
    print(f"Running fio with config: {config}")
    try:
        subprocess.run([
            "fio", config,
            "--output-format=json",
            f"--output={output}"
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running fio: {e}")
        exit(1)

def parse_fio_output(output):
    with open(output, 'r') as f:
        data = json.load(f)

    records = []
    for job in data.get("jobs", []):
        name = job.get("jobname")
        read = job["read"]
        write = job["write"]

        records.append({
            "job": name,
            "read_iops": round(read.get("iops", 0)),
            "read_bw_MBps": round(read.get("bw", 0) / 1024, 2),
            "read_lat_us": round(read.get("lat_ns", {}).get("mean", 0) / 1000, 2),
            "write_iops": round(write.get("iops", 0)),
            "write_bw_MBps": round(write.get("bw", 0) / 1024, 2),
            "write_lat_us": round(write.get("lat_ns", {}).get("mean", 0) / 1000, 2)
        })

    return pd.DataFrame(records)

def log_summary(df):
    timestamp = datetime.datetime.now().isoformat()
    with open(LOG_FILE, "a") as f:
        for _, row in df.iterrows():
            f.write(
                f"[{timestamp}] Job: {row['job']}, "
                f"Read: {row['read_iops']} IOPS, {row['read_bw_MBps']} MB/s, {row['read_lat_us']} µs, "
                f"Write: {row['write_iops']} IOPS, {row['write_bw_MBps']} MB/s, {row['write_lat_us']} µs\n"
            )

def visualize_data(df):
    fig, ax = plt.subplots()
    index = np.arange(len(df))
    bar_width = 0.35

    read_bars = ax.bar(index, df['read_bw_MBps'], bar_width, label='Read BW (MB/s)')
    write_bars = ax.bar(index + bar_width, df['write_bw_MBps'], bar_width, label='Write BW (MB/s)')

    ax.set_xlabel('Job')
    ax.set_ylabel('Bandwidth (MB/s)')
    ax.set_title('FIO Read/Write Bandwidth by Job')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(df['job'], rotation=45)
    ax.legend()

    plt.tight_layout()
    plt.show()

def main():
    parser = argparse.ArgumentParser(description="Run and parse FIO benchmark")
    parser.add_argument('--config', default='nvme_test_win.fio', help='FIO config file')
    parser.add_argument('--output', default='fio_output.json', help='FIO output file (JSON)')
    args = parser.parse_args()

    run_fio(args.config, args.output)
    df = parse_fio_output(args.output)

    print("\nFIO Test Summary:\n----------------")
    print(df.to_string(index=False))

    log_summary(df)
    visualize_data(df)

    print("\nFIO Test Complete")



if __name__ == "__main__":
    main()
