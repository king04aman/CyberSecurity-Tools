# Network Scanner

*This script scans the network for all devices connected to it and lists their IP and MAC addresses.*

## Prerequisites
*The script requires the following dependencies to be installed:*

- Python 3.x
- Scapy
- argparse

## Usage

*To use the script, run it from the command line and provide the target IP address or IP range to scan using the -t or --target option. For example:*
```
python network_scanner.py -t 192.168.1.0/24
```
This will scan all IPs on the 192.168.1.0/24 network and print the results to the console.

## Output
*The script outputs the IP and MAC addresses of all devices found on the network. The output is printed in a tabular format with columns for IP and MAC addresses.*

## License

*This project is licensed under the MIT License - see the [LICENSE.md](../LICENSE) file for details.*