import socket
import argparse
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

parser = argparse.ArgumentParser(description="PortOracle - Port Scanner")
parser.add_argument("--ip", required=True, help="Target IP or hostname")
parser.add_argument("--start", type=int, default=1, help="Start port")
parser.add_argument("--end", type=int, default=1024, help="End port")
parser.add_argument("--timeout", type=float, default=1.0, help="Timeout for each port scan in seconds")

args = parser.parse_args()

def scan_port(ip, port, timeout):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((ip, port))
    sock.close()
    return port, result == 0
    
open_ports = []

with ThreadPoolExecutor(max_workers=100) as executor:

    try:
        futures = {executor.submit(scan_port, args.ip, port, args.timeout): port for port in range(args.start, args.end + 1)}

        for future in as_completed(futures):
            port, is_open = future.result()
            if is_open:

                try:
                    service_name = socket.getservbyport(port, 'tcp')

                except OSError as e:
                    print(f"Warning: Could not determine service for port {port}: {e}")
                    service_name = "unknown"
                
                print(f"Port {port} is OPEN ({service_name})")
                open_ports.append({"port": port, "status": "OPEN", "service": service_name})

    except socket.gaierror:
        print(f"Error: Unable to resolve hostname '{args.ip}'")
        exit(1)

with open("results.json", "w") as file:
    json.dump({"ip": args.ip, "open_ports": open_ports}, file, indent=4)
    print(f"\nResults saved to results.json")