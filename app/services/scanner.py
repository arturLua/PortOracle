import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from app.utils.network import get_service_name
from app.config import DEFAULT_START_PORT, DEFAULT_END_PORT, DEFAULT_TIMEOUT, DEFAULT_WORKERS
from tqdm import tqdm

def scan_port(ip, port, timeout):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((ip, port))
    sock.close()
    return port, result == 0

def run_scan(ip, start_port=DEFAULT_START_PORT, end_port=DEFAULT_END_PORT, timeout=DEFAULT_TIMEOUT):

    open_ports = []

    with tqdm(total= end_port - start_port + 1, desc="Scanning ports...") as pbar:

        with ThreadPoolExecutor(max_workers=DEFAULT_WORKERS) as executor:
            
                futures = {executor.submit(scan_port, ip, port, timeout): port for port in range(start_port, end_port + 1)}
                for future in as_completed(futures):
                    pbar.update(1)
                    port, is_open = future.result()

                    if is_open:
                            service_name = get_service_name(port)
                            open_ports.append({"port": port, "status": "OPEN", "service": service_name})

    return sorted(open_ports, key=lambda x: x["port"])