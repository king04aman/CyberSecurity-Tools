# ARP Spoofing Tool

*This is a simple ARP Spoofing tool written in Python using the scapy library.*

## Usage
*Run the script in a terminal with root privileges.*
```
sudo python arp_spoofing.py -t [target IP] -g [gateway IP]
```

Example: 
```
sudo python arp_spoofing.py -t 192.168.1.10 -g 192.168.1.1
```
*This will start sending spoofed ARP packets to the target and the gateway. To stop the attack, press Ctrl + C. The script will automatically restore the original ARP tables of the target and the gateway.*

## Dependencies
*The script requires the scapy library to be installed. To install it, run the following command:*
```
pip install scapy
```
## Disclaimer
*This tool is for educational purposes only. Use it at your own risk. The author is not responsible for any damages caused by the use of this tool. It is recommended to use this tool only on a test network that you own or have permission to use.*