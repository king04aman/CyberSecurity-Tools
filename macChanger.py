import subprocess
import optparse

def change_mac(interface, new_mac):
    print("[+] Changing MAC for interface " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Specify interface to change MAC for,  use --help for usage")
    parser.add_option("-m", "--mac", dest="new_mac", help="Specify the new MAC , use --help for usage")
    (options, agruments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify interface, use --help for usage")
    elif not options.new_mac:
        parser.error("[-] Please specify MAC , use --help for usage")
    return options



options = get_arguments()
change_mac(options.interface, options.new_mac)