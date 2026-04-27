import socket

ip = "scanme.nmap.org"
portas = [22, 80, 443, 8080]

for porta in portas:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    resultado = sock.connect_ex((ip, porta))

    if resultado == 0:
        print(f"Porta {porta} está ABERTA")
    else:
        print(f"Porta {porta} está FECHADA")

    sock.close()