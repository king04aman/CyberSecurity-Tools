from socket import *  # importing everything from bluit in python module socket
import optparse  # importing optparse library for accepting arguments
import threading  # threading library for simultaneous execution of program or functions


def portScan(host, port):
    try:
        s = socket(AF_INET, SOCK_STREAM)  # creating an object of class socket AF_INET for ipv4 and AF_INET6 for ipv6
        # SOCK_STREAM is for tcp(protocol) and SOCK_DGRAM id for udp(protocol)
        s.connect((host, int(port)))  # connecting to the socket with target host and port
        print(host + " tcp/" + str(port) + " open")
        s.close()

    except:
        print(host + " tcp/" + str(port) + " closed")  # print this if unable to connect (meaning port closed)


def main():
    parser = optparse.OptionParser("uasge%prog " + "-H <specify target host> -p <specify ports separated by ',' > ")
    parser.add_option("-H", '--host', dest='targethost', type='string', help='specify target hsot')
    parser.add_option("-p", "--ports", dest='targetports', type='string', help='specify target ports separated by "," ')

    option, args = parser.parse_args()  # this functions returns the arguments received inside object options

    thost = option.targethost  # accessing arguments
    tports = str(option.targetports).split(",")

    if thost == None or tports[0] == None:
        print(parser.usage)  # prints the usage defined inside the OptionParser class Above as string
        exit(0)

    setdefaulttimeout(1)  # close connection if no response is received
    host_ip = gethostbyname(thost)  # get the target ip using target domain

    for port in tports:
        t = threading.Thread(target=portScan,
                             args=(thost, port))  # creating a portScann Function thread for each port in port list
        t.start()  # Starting the thread


main()