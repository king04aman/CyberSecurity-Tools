# HTTP Packet Sniffer

*This is a Python script that sniffs HTTP packets on a given interface and prints any HTTP requests and potential username/passwords found in the packet payload.*

## Requirements

- Python 3.x
- Scapy module (pip install scapy)

## Usage
*Run the script using the following command:*
```
python http_sniffer.py -i <interface>
```

*Replace `<interface>` with the name of the interface on which you want to sniff packets.*

*The script will start sniffing packets and print any HTTP requests and potential username/passwords found in the packet payload.*

## Note
*This script should be used for educational purposes only. Sniffing network traffic without authorization is illegal in many jurisdictions.*