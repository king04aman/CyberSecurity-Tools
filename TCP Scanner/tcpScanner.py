import socket
import optparse
import threading


def port_scan(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((host, int(port)))
            print(f"{host} tcp/{port} open")

    except (socket.timeout, ConnectionRefusedError):
        print(f"{host} tcp/{port} closed")


def main():
    parser = optparse.OptionParser(
        "usage%prog -H <specify target host> -p <specify ports separated by ','>")
    parser.add_option("-H", '--host', dest='target_host',
                      type='string', help='specify target host')
    parser.add_option("-p", "--ports", dest='target_ports', type='string',
                      help='specify target ports separated by ","')

    options, args = parser.parse_args()

    if not options.target_host or not options.target_ports:
        print(parser.usage)
        exit()

    host_ip = socket.gethostbyname(options.target_host)
    ports = options.target_ports.split(",")

    for port in ports:
        t = threading.Thread(target=port_scan, args=(host_ip, port))
        t.start()


if __name__ == "__main__":
    main()
