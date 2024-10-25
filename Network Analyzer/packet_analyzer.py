import socket
import os
import sys
import struct
import binascii


def analyze_udp_header(data_recv):
    udp_hdr = struct.unpack('!4H', data_recv[:8])
    src_port = udp_hdr[0]
    dst_port = udp_hdr[1]
    length = udp_hdr[2]
    checksum = udp_hdr[3]
    data = data_recv[8:]

    print('_________________UDP Header:________________')
    print('Source Port: ', src_port)
    print('Destination Port: ', dst_port)
    print('Length: ', length)
    print('Checksum: ', checksum, '\n')


def analyze_tcp_header(data_recv):
    tcp_hdr = struct.unpack('!2H2I4H', data_recv[:20])
    src_port = tcp_hdr[0]
    dst_port = tcp_hdr[1]
    seq_num = tcp_hdr[2]
    ack_num = tcp_hdr[3]
    data_offset = tcp_hdr[4] >> 12
    reserved = (tcp_hdr[4] >> 6) & 0x03ff
    flags = tcp_hdr[4] & 0x003f
    window = tcp_hdr[5]
    checksum = tcp_hdr[6]
    urg_ptr = tcp_hdr[7]
    data = data_recv[20:]

    urg = bool(flags & 0x0020)
    ack = bool(flags & 0x0010)
    psh = bool(flags & 0x0008)
    rst = bool(flags & 0x0004)
    syn = bool(flags & 0x0002)
    fin = bool(flags & 0x0001)

    print('_________________TCP Header:________________')
    print('Source Port: ', src_port)
    print('Destination Port: ', dst_port)
    print('Sequence Number: ', seq_num)
    print('Acknowledgement Number: ', ack_num)
    print('Data Offset: ', data_offset)
    print('Reserved: ', reserved)
    print('Flags: ', flags)
    print('Window: ', window)
    print('Checksum: ', checksum)
    print('Urgent Pointer: ', urg_ptr, '\n')
    print("Flags: ")
    print("URG: ", urg)
    print("ACK: ", ack)
    print("PSH: ", psh)
    print("RST: ", rst)
    print("SYN: ", syn)
    print("FIN :", fin)


def analyze_ip_header(data_recv):
    ip_hdr = struct.unpack('!6H4s4s', data_recv[:20])
    ver = ip_hdr[0] >> 12
    ihl = (ip_hdr[0] >> 8) & 0x0f
    tos = ip_hdr[0] & 0x00ff
    tot_len = ip_hdr[1]
    ip_id = ip_hdr[2]
    flags = ip_hdr[3] >> 13
    frag_offset = ip_hdr[3] & 0x1fff
    ip_ttl = ip_hdr[4] >> 8
    ip_proto = ip_hdr[4] & 0x00ff
    checksum = ip_hdr[5]
    src_addr = socket.inet_ntoa(ip_hdr[6])
    dst_addr = socket.inet_ntoa(ip_hdr[7])
    data = data_recv[20:]

    print('_________________IP Header:________________')
    print('Version: ', ver)
    print('IP Header Length: ', ihl)
    print('Type of Service: ', tos)
    print('Total Length: ', tot_len)
    print('Identification: ', ip_id)
    print('Flags: ', flags)
    print('Fragment Offset: ', frag_offset)
    print('Time to Live: ', ip_ttl)
    print('Protocol: ', ip_proto)
    print('Header Checksum: ', checksum)
    print('Source Address: ', src_addr)
    print('Destination Address: ', dst_addr, '\n')

    if ip_proto == 6:
        tcp_udp = "TCP"
    elif ip_proto == 17:
        tcp_udp = "UDP"
    else:
        tcp_udp = "Other"

    return data, tcp_udp

def analyze_ether_header(data_recv):
    ip_bool = False

    eth_hdr = struct.unpack('!6s6sH', data_recv[:14])
    dst_mac = binascii.hexlify(eth_hdr[0]).decode('utf-8')
    src_mac = binascii.hexlify(eth_hdr[1]).decode('utf-8')
    proto = eth_hdr[2] >> 8
    data = data_recv[14:]
    print('______________Ethernet Header:______________')
    print('Destination MAC: {}:{}:{}:{}:{}:{}'.format(
        dst_mac[0:2], dst_mac[2:4], dst_mac[4:6], dst_mac[6:8], dst_mac[8:10], dst_mac[10:12]))
    print('Source MAC: {}:{}:{}:{}:{}:{}'.format(
        src_mac[0:2], src_mac[2:4], src_mac[4:6], src_mac[6:8], src_mac[8:10], src_mac[10:12]))
    print('Protocol: {}\n'.format(proto))

    if proto == 0x0800:
        ip_bool = True
    return data, ip_bool

def main():
    sniffer_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    sniffer_socket.bind(("YOUR_INTERFACE_IP_ADDRESS", 0))  # Replace with the appropriate interface IP address

    sniffer_socket.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    sniffer_socket.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    while True:
        data_recv, addr = sniffer_socket.recvfrom(65535)
        os.system('cls' if os.name == 'nt' else 'clear')

        data_recv, ip_bool = analyze_ether_header(data_recv)
        if ip_bool:
            data_recv, tcp_udp = analyze_ip_header(data_recv)
        else:
            continue

        if tcp_udp == "TCP":
            analyze_tcp_header(data_recv)
        elif tcp_udp == "UDP":
            analyze_udp_header(data_recv)



if __name__ == '__main__':
    main()
