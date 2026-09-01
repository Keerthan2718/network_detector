from system import get_hostname
from network import get_arp_table, get_ipv4, get_network
from network import get_subnet_mask
from network import get_default_gateway
from network import get_dns_server
from ports import get_listening_ports, test_connection




def main():
    hostname = get_hostname()
    ip_address = get_ipv4()
    subnet_mask = get_subnet_mask()
    gateway = get_default_gateway()
    dns_server = get_dns_server()
    arp_table = get_arp_table()
    ports = get_listening_ports()
    network = get_network(ip_address, subnet_mask)


    print("==============================")
    print("       NETWORK DETECTIVE")
    print("==============================")
    print()
    print("Hostname:", hostname)
    print("IPv4 Address:", ip_address)
    print("Subnet Mask:", subnet_mask)
    print("Default Gateway:", gateway)
    print("DNS Server:", dns_server)
    print()
    print("ARP TABLE")
    print("------------------------------")
    print(f"{'IP':<18}MAC")

    for ip, mac in arp_table:
        print(f"{ip:<18}{mac}")

    for port, pid in ports:
        print(f"{port:<10}{pid}")

    print()
    print("TEST CONNECTION")
    print("------------------------------")

    target = input("Target: ")
    port = int(input("Port: "))

    status = test_connection(target, port)

    print("Status:", status)

    print("Network:", network)
    print("Network Address:", network.network_address)
    print("Broadcast Address:", network.broadcast_address)

if __name__ == "__main__":
    main()