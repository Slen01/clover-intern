import platform
import subprocess
import socket

def is_host_alive(ip_address):
    """
    Ping the target IP address to check if it is alive.
    """
    # Determine the parameter for count depending on OS
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", ip_address]

    try:
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        if result.returncode == 0:
            print(f"\n✅ {ip_address} is alive.\n")
            return True
        else:
            print(f"\n❌ {ip_address} is not reachable.\n")
            return False
    except Exception as e:
        print(f"\n⚠️ Error pinging {ip_address}: {e}\n")
        return False

def scan_common_ports(ip_address):
    """
    Scan a list of common ports and print which ones are open.
    """
    common_ports = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS",
        3306: "MySQL",
        3389: "RDP",
        8080: "HTTP-Alt"
    }

    print("🔍 Scanning common ports...\n")

    for port, service in common_ports.items():
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)  # Half-second timeout per port
                result = sock.connect_ex((ip_address, port))
                if result == 0:
                    print(f"✅ Port {port} ({service}) is OPEN.")
                else:
                    print(f"❌ Port {port} ({service}) is CLOSED.")
        except Exception as e:
            print(f"⚠️ Error scanning port {port}: {e}")

if __name__ == "__main__":
    ip = input("Enter the IP address to scan: ").strip()

    if ip:
        if is_host_alive(ip):
            scan_common_ports(ip)
        else:
            print("Host appears to be offline. Skipping port scan.")
    else:
        print("❗ No IP address entered.")
