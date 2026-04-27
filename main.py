import socket

ip = "scanme.nmap.org"
ports = [22, 80, 443, 8080]

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((ip, port))

    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")

    sock.close()