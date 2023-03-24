import argparse
from scapy.all import sniff, Raw
from scapy.layers import http


def get_interface() -> str:
    """Parses command-line arguments and returns interface name to sniff packets."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface",
                        help="Specify interface on which to sniff packets")
    args = parser.parse_args()
    if not args.interface:
        parser.error("Please specify an interface to sniff packets.")
    return args.interface


def process_packet(packet) -> None:
    """Processes the sniffed packet and prints any HTTP requests and potential username/passwords."""
    if packet.haslayer(http.HTTPRequest):
        print(
            f"[+] Http Request >> {packet[http.HTTPRequest].Host}{packet[http.HTTPRequest].Path}")
        if packet.haslayer(Raw):
            load = packet[Raw].load.decode()
            keys = ["username", "password", "pass", "email"]
            for key in keys:
                if key in load:
                    print(f"\n\n\n[+] Possible {key} >> {load}\n\n\n")
                    break


def sniff_packets(interface: str) -> None:
    """Sniffs packets on the given interface and processes them using process_packet function."""
    sniff(iface=interface, store=False, prn=process_packet)


if __name__ == '__main__':
    iface = get_interface()
    sniff_packets(iface)
