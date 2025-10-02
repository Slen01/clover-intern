IP TRACER HELPS FIND IP ADDRESS , WHETHER ITS ALIVE OR NOT AND ALSO HELPS FIND OPEN COMMON TCP PORTS


# 🛰️ IP Tracer

## 📘 Overview
**IP Tracer** is a Python-based tool that uses the built-in **socket** module to:
- Find the **IP address** of any given domain or hostname  
- Check **whether the target is alive (reachable)**  
- Detect **open common TCP ports** for basic network analysis  

> ⚡ This project is ideal for students, ethical hackers, and cybersecurity learners.

---

## ⚙️ Features

### 🔍 1. IP Address Finder
- Resolves hostnames to IP addresses using `socket.gethostbyname()`
- Helps identify the exact IP of a domain before performing scans  

### 🌐 2. Host Availability Checker
- Checks if the given host is alive by attempting TCP connections  
- Uses port probing to verify reachability  

### 🔓 3. Common TCP Port Scanner
- Scans a predefined list of **common ports** (e.g., 21, 22, 25, 53, 80, 443, etc.)  
- Reports which ports are open using `socket.connect_ex()`  

---

## 🧠 About the `socket` Module
The `socket` module is a **Python standard library** that enables low-level network communication.

### 📘 Key Functions Used
| Function | Description |
|-----------|--------------|
| `socket.socket()` | Creates a new socket object |
| `socket.gethostbyname(host)` | Returns the IP address of the given hostname |
| `socket.connect_ex((host, port))` | Attempts to connect to a given port; returns 0 if open |
| `socket.setdefaulttimeout(seconds)` | Sets a timeout for network operations |

---

## 🧩 How It Works

1. **User Input:** Enter the target hostname or IP.  
2. **IP Resolution:** Converts hostname to IP using `socket.gethostbyname()`.  
3. **Availability Check:** Tests if the target responds on common ports.  
4. **Port Scan:** Iterates through popular TCP ports to detect open ones.  

---

## 💻 Example Usage

Run the script:
```bash
python ip_tracer.py
[+] Target Host: example.com
[+] IP Address: 93.184.216.34
[✓] Host is Alive
[+] Scanning Common Ports...
[OPEN] 80 (HTTP)
[CLOSED] 22 (SSH)
[OPEN] 443 (HTTPS)
