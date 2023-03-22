# MAC Address Changer

*This script changes the MAC address of a network interface. It takes two command line arguments:*

- -i, --interface: the name of the interface for which the MAC address needs to be changed (e.g. eth0, wlan0, etc.)
- -m, --mac: the new MAC address that needs to be set (in the format XX:XX:XX:XX:XX:XX)

## Requirements

*This script requires Python 3 and the optparse module.*

## Usage

*To run the script, open a terminal and navigate to the directory where the script is saved. Then run the following command:*
```
python mac_changer.py -i [interface_name] -m [new_mac_address]
```

Make sure to replace [interface_name] with the name of the interface for which you want to change the MAC address, and [new_mac_address] with the new MAC address that you want to set.

Example:
```
python mac_changer.py -i eth0 -m 00:11:22:33:44:55
```

This will change the MAC address of the eth0 interface to 00:11:22:33:44:55.

## Disclaimer

*This script is intended for educational purposes only. Use at your own risk. The author is not responsible for any damage caused by this script.*