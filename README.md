<h1 align="center">PortOracle</h1>

###

<p>
PortOracle is a simple yet effective network utility designed to scan and detect the status of specific ports on a target machine. It uses Python's `socket` library to perform TCP connection attempts and reports whether each port is open or closed.
</p>

<h1>Features</h1>

- Simple and straightforward port scanning
- Fast scanning with configurable timeout
- Clear output reporting open/closed ports
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

Run the scanner:

```bash
python main.py
```

### Customizing the Scan

Edit `main.py` to modify the target and ports:

```python
ip = "scanme.nmap.org"  # Change target host
ports = [22, 80, 443, 8080]  # Change ports to scan
```

**Current configuration:**
- **Target:** `scanme.nmap.org` (a legal testing host provided by nmap.org)
- **Ports:** 22 (SSH), 80 (HTTP), 443 (HTTPS), 8080 (HTTP alternate)
- **Timeout:** 1 second per connection attempt

### Output Example

```
Port 22 is OPEN
Port 80 is OPEN
Port 443 is CLOSED
Port 8080 is CLOSED
```

## Configuration

To customize the scanner for your needs:

1. **Change the target IP/hostname:** Modify the `ip` variable
2. **Change ports:** Update the `ports` list with desired port numbers
3. **Adjust timeout:** Modify `sock.settimeout(1)` to a different value (in seconds)

## Legal Notice

> [!NOTE] 
> Only scan networks and hosts for which you have **EXPLICIT PERMISSION**. Unauthorized port scanning may be illegal in your jurisdiction. This tool is provided for educational and authorized security testing purposes only.

The default configuration scans `scanme.nmap.org`, which is provided by nmap.org specifically for testing purposes.