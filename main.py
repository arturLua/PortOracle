import socket
import argparse

parser = argparse.ArgumentParser(description="PortOracle - Port Scanner")
parser.add_argument("--ip", required=True, help="Target IP or hostname")
parser.add_argument("--start", type=int, default=1, help="Start port")
parser.add_argument("--end", type=int, default=1024, help="End port")
args = parser.parse_args()
print(args)

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    sock.close()
    return result == 0

for port in range(args.start, args.end + 1):
    if scan_port(args.ip, port):
        print(f"Port {port} is OPEN")