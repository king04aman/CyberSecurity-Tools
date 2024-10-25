# Network Packet Analyzer

This Python script functions as a network packet analyzer, capturing and analyzing Ethernet, IP, TCP, and UDP headers from network packets. It provides detailed information about each packet received, helping users understand network traffic.

## Features

- Captures and analyzes Ethernet frames.
- Parses and displays IP header information.
- Extracts and presents TCP and UDP header details.
- Continuously monitors and displays packet information in real-time.

## Requirements

To run this script, you need:

- Python 3.x
- Administrative privileges to capture packets on the network interface.

## Installation

Make sure you have Python installed on your system. Clone or download this repository and navigate to the project directory.

## Usage

1. **Run the Script**: Execute the script with administrative privileges. You might need to replace `"YOUR_INTERFACE_IP_ADDRESS"` in the `bind()` method with the appropriate IP address of the network interface you wish to capture traffic from.

   ```bash
   python packet_analyzer.py
   ```

2. **View Output**: The script will continuously capture packets and display the parsed headers in the console.

3. **Clear Console**: The output is cleared each time a new packet is captured, providing a live view of the latest packet data.

## Code Explanation

- **Ethernet Header Analysis**: The script begins by analyzing the Ethernet header, extracting source and destination MAC addresses and protocol type.
  
- **IP Header Analysis**: If the Ethernet frame contains an IP packet, the script parses the IP header and identifies the protocol (TCP or UDP).

- **TCP/UDP Header Analysis**: Based on the identified protocol, the script parses either the TCP or UDP header and displays relevant information such as source/destination ports, sequence numbers, and flags.

## Running on Different Platforms

- **Windows**: Make sure to run the script in an elevated command prompt (Run as Administrator).
  
- **Linux**: You may need to run the script with `sudo` to capture packets:

   ```bash
   sudo python packet_analyzer.py
   ```

## Limitations

- This script requires administrative privileges to capture packets.
- It may not work on certain systems where raw socket access is restricted.
- The script is designed for educational purposes and may require modifications for production use.

## License

This project is licensed under the MIT License. Feel free to modify and use it in your own projects!