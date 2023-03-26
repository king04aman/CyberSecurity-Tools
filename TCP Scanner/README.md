# Port Scanner

*This Python script performs a simple TCP port scan on a given host and ports.*

## Usage
```
The program takes two command line arguments:
```

- -H, --host: specify target host
- -p, --ports: specify target ports separated by commas (,)

*The -H option is used to specify the target host to scan and the -p option is used to specify the target ports separated by a comma.*

## Example
To scan port 80 on example.com, run the following command:
```
python port_scanner.py -H example.com -p 80
```

To scan ports 80, 443, and 8080 on example.com, run the following command:
```
python port_scanner.py -H example.com -p 80,443,8080
```
## Output

*The script will output whether each specified port is open or closed on the target host. If a port is open, the output will show the host IP address, the port number, and that the port is open. If a port is closed, the output will show the host IP address, the port number, and that the port is closed.*

## Implementation

*The script uses the socket module to establish a TCP connection to the target host and port. It creates a separate thread for each port to be scanned in order to speed up the process. If a connection cannot be established within one second or the connection is refused, the port is considered closed.*

