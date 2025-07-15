# System-Testing

Automated system-level testing framework designed for hardware and software validation in embedded and endpoint environments. This project demonstrates proficiency in Python-based test automation, CI integration, and data-driven diagnostics.

---

## 🔍 Overview

This framework is built to automate testing of system-level components such as CPU telemetry, power consumption, and thermal profiles. It is designed for modularity, reusability, and data visibility—ideal for environments where hardware/software integration needs repeatable, scalable validation.

Key goals:
- Enable repeatable functional and stress testing
- Automate test execution and data capture
- Validate hardware/firmware behavior under load
- Integrate with CI tools like Jenkins for continuous test feedback

---

## ⚙️ Features

- ✅ Modular Python test scripts with CLI interface  
- ✅ Telemetry checks: temperature, voltage, frequency  
- ✅ JSON-based logging of test results  
- ✅ Jenkins-compatible structure for pipeline execution  
- ✅ Utility functions for statistical analysis using NumPy/Pandas  
- ✅ Color-coded terminal output for quick test summaries  

---

## 🧰 Tech Stack

- **Language:** Python 3.10  
- **Libraries:** `subprocess`, `argparse`, `pandas`, `numpy`, `json`, `matplotlib`  
- **Tools:**  Git, Jenkins 

---

## 📂 Project Structure

(img/Simple_Fio-test.png)
System-Testing/
│
├── test_runner.py # Main entry point
├── hardware_tests/ # Contains CPU/memory/power test scripts
├── lib/ # Utility functions and log formatter
├── config/ # Test config and thresholds
├── logs/ # JSON test result output
└── README.md


---

## 🚀 Getting Started

### Requirements
- Python 3.10+
- Install dependencies:
pip install -r requirements.txt


### Run a test
python3 test_runner.py --target cpu --duration 60


### View logs
Logs are saved as JSON in `/logs` and can be parsed for dashboards or trend analysis.

---

## 📈 Sample Output

![Sample output](https://github.com/CyberHuey/System-Testing/assets/sample_output.png)

---

## ✅ Why It Matters

This project showcases:
- Hands-on experience with Python test automation
- Real-world validation logic (CPU, memory, temperature, voltage)
- Use of statistical libraries for performance tracking
- CI pipeline readiness and modular structure

Ideal for roles in test engineering, validation, SDET, or DevOps with a hardware interface.

---

## 📬 Contact

Ralph Walker II  
📧 ralph.o.walkerii@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/ralph-walker-ii-a704a1a6)
