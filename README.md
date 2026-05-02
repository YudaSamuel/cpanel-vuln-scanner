# cpanel-vuln-scanner

A fully automated tool designed to scan target domains or IP addresses and provide detailed insights about their status, configurations, and potential vulnerabilities.

---

## ⚡ Features

* 🔍 Automatic scanning of domains and IP addresses
* ⚙️ Detection of misconfigurations and weak points
* 🛡️ Identification of potential vulnerabilities
* 🚀 Multi-threaded scanning for high performance
* 📄 Optional output file saving
* 🧩 Simple and flexible CLI interface

---

## 📦 Requirements

* Python 3.8 or higher

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### 🔹 Basic Usage

Scan targets from a file:

```bash
python check.py --input domains.txt
```

---

### 🔹 Save Results to File

```bash
python check.py --input domains.txt --output results.txt
```

---

### 🔹 Increase Thread Count (Faster Scanning)

```bash
python check.py --input domains.txt --threads 50
```

---

### 🔹 Full Example

```bash
python scanner.py --input domains.txt --output results.txt --threads 50
```

---

## ⚙️ Arguments

| Argument    | Required | Description                                  |
| ----------- | -------- | -------------------------------------------- |
| `--input`   | ✅ Yes    | File containing target domains or IPs        |
| `--output`  | ❌ No     | Output file (default: `cve_active.txt`)      |
| `--threads` | ❌ No     | Number of concurrent threads (default: `10`) |

---

## 📁 Example Input File (domains.txt)

```
example.com
google.com
1.1.1.1
testsite.org
```

---

## 📊 Output

* Results will be printed to the console
* If `--output` is specified, results will also be saved to a file

Example output:

```
[+] example.com -> Vulnerable
[-] google.com -> Not Vulnerable
[!] testsite.org -> Timeout / Error
```

---

## ⚠️ Disclaimer

This tool is developed for **educational and authorized security testing purposes only**.
You are responsible for how you use it. Do not scan or attack systems without explicit permission.

---

## 📌 Notes

* Use a higher thread count carefully to avoid network instability
* Large scans may take time depending on target size and network conditions
* Always ensure you have permission before scanning targets

---
