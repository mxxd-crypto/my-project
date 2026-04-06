import socket

def scan_port(ip, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) # Wait 1 second for a response
        
        # Try to connect to the port
        result = sock.connect_ex((ip, port))
        
        if result == 0:
            print(f"🔓 Port {port}: OPEN")
        sock.close()
    except Exception as e:
        print(f"Error: {e}")

# Try scanning a common web port on a test site
target_ip = "8.8.8.8"  # Google's DNS
common_ports = [21, 22, 80, 443]

print(f"Scanning {target_ip}...")
for port in common_ports:
    scan_port(target_ip, port)