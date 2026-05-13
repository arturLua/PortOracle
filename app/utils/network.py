import socket

def resolve_hostname(hostname):
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        raise ValueError(f"Error: Unable to resolve hostname '{hostname}'")

def get_service_name(port):
    try:
        return socket.getservbyport(port, 'tcp')
    except OSError:
        return "unknown"