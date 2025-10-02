# 🛰️ IP Tracer

## 📘 Overview
**IP Tracer** is a simple Python tool that uses the built-in **socket**, **subprocess**, and **platform** modules to:
- Check if an **IP address is alive** using system-level ping commands  
- **Scan common TCP ports** to identify open network services  
- Provide quick insights into host reachability and service availability  

This project is perfect for **beginners**, **cybersecurity learners**, and **network enthusiasts** who want to understand how basic network scanning works.

---

## ⚙️ Features

### 🌐 1. Host Availability Check
- Uses the `ping` command to verify if a given IP address is alive.  
- Automatically detects the user’s OS (Windows/Linux/Mac) and uses the correct ping parameter (`-n` or `-c`).  
- Prints a clear message whether the host is **alive** or **not reachable**.

### 🔍 2. Common TCP Port Scanner
- Scans a predefined set of **well-known ports**, including:
  - 21 (FTP)
  - 22 (SSH)
  - 23 (Telnet)
  - 25 (SMTP)
  - 53 (DNS)
  - 80 (HTTP)
  - 110 (POP3)
  - 143 (IMAP)
  - 443 (HTTPS)
  - 3306 (MySQL)
  - 3389 (RDP)
  - 8080 (HTTP-Alt)  

- Uses the **socket** module’s `connect_ex()` method to test if each port is open.  
- Displays ✅ **OPEN** or ❌ **CLOSED** for every port scanned.

---

## 🧠 Module Information

### 🧩 `platform`
- Detects the operating system to determine correct command-line arguments for ping.

### ⚙️ `subprocess`
- Runs the `ping` command in the background and captures its output to check reachability.

### 🌐 `socket`
- Creates a TCP socket connection to test if specific ports are open or closed.  
- Provides low-level network access without external libraries.

---

## 🧩 How It Works
1. The user inputs a target **IP address**.  
2. The script runs a **ping test** using `subprocess.run()` to see if the host is alive.  
3. If the host is reachable, it proceeds to **scan common TCP ports** using the `socket` module.  
4. The tool prints real-time port scan results for every tested service.  

---

## 💻 Example Usage

Run the script in your terminal:
```bash
python ip_tracer.py

output
Enter the IP address to scan: 8.8.8.8

✅ 8.8.8.8 is alive.

🔍 Scanning common ports...

✅ Port 80 (HTTP) is OPEN.
❌ Port 22 (SSH) is CLOSED.
✅ Port 443 (HTTPS) is OPEN.

if it is offline
Enter the IP address to scan: 10.10.10.10

❌ 10.10.10.10 is not reachable.

Host appears to be offline. Skipping port scan.

