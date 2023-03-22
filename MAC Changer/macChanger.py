import subprocess
import optparse


def change_mac(interface, new_mac):
    """
    Change the MAC address of the specified interface to the new MAC address.
    """
    print("[+] Changing MAC for interface " + interface + " to " + new_mac)

    # Disable the specified interface
    subprocess.call(["ifconfig", interface, "down"])

    # Set the new MAC address for the specified interface
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])

    # Enable the specified interface
    subprocess.call(["ifconfig", interface, "up"])


def get_arguments():
    """
    Get the command line arguments provided by the user.
    """
    parser = optparse.OptionParser()

    # Add the interface and MAC options to the parser
    parser.add_option("-i", "--interface", dest="interface",
                      help="Specify interface to change MAC for, use --help for usage")
    parser.add_option("-m", "--mac", dest="new_mac",
                      help="Specify the new MAC , use --help for usage")

    (options, agruments) = parser.parse_args()

    # Validate the options provided by the user
    if not options.interface:
        parser.error("[-] Please specify interface, use --help for usage")
    elif not options.new_mac:
        parser.error("[-] Please specify MAC, use --help for usage")

    return options


# Get the user provided arguments
options = get_arguments()

# Change the MAC address of the specified interface to the new MAC address
change_mac(options.interface, options.new_mac)
