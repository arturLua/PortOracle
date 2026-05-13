<h1 align="center">PortOracle</h1>

<p>
PortOracle is a network port scanner built with Python. It uses concurrent threads to perform TCP connection attempts and reports open ports along with their associated services.
</p>

## Project Structure
```bash
portoracle/
├── app/
│   ├── config.py          # Default configuration constants
│   ├── services/
│   │   └── scanner.py     # Core scanning logic
│   └── utils/
│       ├── network.py     # Hostname resolution and service detection
│       └── file.py        # JSON output handling
└── cli.py                 # Entry point
```

## Requirements

- Python 3.6+

## Installation

1. Clone the repository:
```bash
git clone <repository_url>
cd PortOracle
```

2. No additional packages required.

## Usage

```bash
python cli.py --ip <target_ip_or_hostname> [--start <start_port>] [--end <end_port>] [--timeout <seconds>] [--output <file>]
```

### Arguments

- `--ip`: Target IP address or hostname (required)
- `--start`: Starting port number (default: 1)
- `--end`: Ending port number (default: 1024)
- `--timeout`: Connection timeout in seconds (default: 1.0)
- `--output`: Output file path (default: results.json)

### Examples

```bash
# Scan default port range (1-1024)
python cli.py --ip scanme.nmap.org

# Scan custom port range
python cli.py --ip 192.168.1.1 --start 20 --end 500

# Scan with custom timeout and output file
python cli.py --ip 192.168.1.1 --timeout 0.5 --output scan.json
```

### JSON Output

Results are saved with the following structure:

```json
{
    "ip": "192.168.1.1",
    "open_ports": [
        {
            "port": 22,
            "status": "OPEN",
            "service": "ssh"
        }
    ]
}
```

## Legal Notice

> [!NOTE]
> Only scan networks and hosts for which you have **EXPLICIT PERMISSION**. Unauthorized port scanning may be illegal in your jurisdiction. This tool is provided for educational and authorized security testing purposes only.

The examples use `scanme.nmap.org`, provided by nmap.org specifically for testing purposes.