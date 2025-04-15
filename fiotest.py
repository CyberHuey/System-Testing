import subprocess
import json
import datetime

FIO_CONFIG = "nvme_test_win.fio" # nvme_test.fio Linux | nvme_test_win.fio 
FIO_OUTPUT = "fio_output.json"
LOG_FILE = "fio_summary_log.txt"

def run_fio():
    print(f"Running fio with config: {FIO_CONFIG}")
    try:
        subprocess.run([
            "fio", FIO_CONFIG,
            "--output-format=json",
            f"--output={FIO_OUTPUT}"
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running fio: {e}")
        exit(1)

def parse_fio_output():
    with open(FIO_OUTPUT, 'r') as f:
        data = json.load(f)

    logDB = []
    for job in data.get("jobs", []):
        name = job.get("jobname")
        read_iops = job["read"].get("iops", 0)
        read_bw = job["read"].get("bw", 0)  # in KB/s
        read_lat = job["read"].get("lat_ns", {}).get("mean", 0)

        write_iops = job["write"].get("iops", 0)
        write_bw = job["write"].get("bw", 0)
        write_lat = job["write"].get("lat_ns", {}).get("mean", 0)

        summary = {
            "job": name,
            "read_iops": round(read_iops),
            "read_bw_MBps": round(read_bw / 1024, 2),
            "read_lat_us": round(read_lat / 1000, 2),
            "write_iops": round(write_iops),
            "write_bw_MBps": round(write_bw / 1024, 2),
            "write_lat_us": round(write_lat / 1000, 2),
        }

        logDB.append(summary)

    return logDB

def log_summary(logDB):
    timestamp = datetime.datetime.now().isoformat()
    with open(LOG_FILE, "a") as f:
        for s in logDB:
            line = (
                f"[{timestamp}] Job: {s['job']}, "
                f"Read: {s['read_iops']} IOPS, {s['read_bw_MBps']} MB/s, {s['read_lat_us']} µs, "
                f"Write: {s['write_iops']} IOPS, {s['write_bw_MBps']} MB/s, {s['write_lat_us']} µs\n"
            )
            f.write(line)

def main():
    run_fio()
    results = parse_fio_output()
    print("\nFIO Test Summary:\n----------------")
    for r in results:
        print(f"Job: {r['job']}")
        print(f"  Read : {r['read_iops']} IOPS | {r['read_bw_MBps']} MB/s | {r['read_lat_us']} µs latency")
        print(f"  Write: {r['write_iops']} IOPS | {r['write_bw_MBps']} MB/s | {r['write_lat_us']} µs latency")
        print("-" * 40)

    log_summary(results)

if __name__ == "__main__":
    main()