<h1 align="center">PortOracle</h1>

###

<p>
PortOracle is a simple yet effective network utility designed to scan and detect the status of specific ports on a target machine. It uses Python's `socket` library to perform TCP connection attempts and reports whether each port is open or closed.
</p>

<h1>Features</h1>

- Simple and straightforward
- Fast concurrent scanning using multiple threads for efficient port detection
- Configurable timeout for connection attempts
- Clear output reporting open ports to console and exported to a JSON file
- Customizable target hosts and ports

## Requirements

- Python 3.6+

## Installation

1. Clone the repository:
```bash
git clone <repository_url>
cd PortOracle
```

2. No additional packages need to be installed.

## Usage

Run the scanner with command-line arguments:

```bash
python main.py --ip <target_ip_or_hostname> [--start <start_port>] [--end <end_port>]
```

### Examples

- Scan ports 1-1024 on a specific host:
```bash
python main.py --ip scanme.nmap.org
```

- Scan a custom port range:
```bash
python main.py --ip 192.168.1.1 --start 20 --end 100
```

- Scan a single port:
```bash
python main.py --ip example.com --start 80 --end 80
```

### Customizing the Scan

The scanner accepts the following arguments:

- `--ip`: Target IP address or hostname (required)
- `--start`: Starting port number (default: 1)
- `--end`: Ending port number (default: 1024)

**Current default configuration:**
- **Target:** Specified via `--ip` argument
- **Port range:** 1-1024
- **Timeout:** 1 second per connection attempt

### Output Example

```
Port 22 is OPEN
Port 80 is OPEN
Port 443 is CLOSED
Port 8080 is CLOSED
...
```

### JSON Output

Results are saved to `results.json` with the following structure:

```json
{
    "ip": "scanme.nmap.org",
    "open_ports": [
        {
            "port": 22,
            "status": "OPEN",
            "service": "ssh"
        }
    ]
}
```

## Configuration

To customize the scanner for your needs:

1. **Change the target IP/hostname:** Use the `--ip` argument
2. **Change port range:** Use `--start` and `--end` arguments
3. **Adjust timeout:** Currently fixed at 1 second per connection attempt; modify `sock.settimeout(1)` in `main.py` if needed
4. **Concurrency:** The scanner uses currently up to 100 concurrent threads for faster scanning; modify `max_workers=100` in `main.py` if needed

## Legal Notice

> [!NOTE] 
> Only scan networks and hosts for which you have **EXPLICIT PERMISSION**. Unauthorized port scanning may be illegal in your jurisdiction. This tool is provided for educational and authorized security testing purposes only.

The examples given here scans `scanme.nmap.org`, which is provided by nmap.org specifically for testing purposes.