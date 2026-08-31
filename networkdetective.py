import socket
import subprocess
import ipaddress

def get_hostname():
    hostname = socket.gethostname()
    return hostname

def get_ipv4():
    hostname = socket.gethostname()
    ip_address=socket.gethostbyname(hostname)
    return ip_address

def get_subnet_mask():
    output = subprocess.check_output(
        ["ipconfig"],
        text=True
    )

    for line in output.splitlines():
        if "Subnet Mask" in line:
            return line.split(":")[-1].strip()

    return "Not found"

def get_default_gateway():
    output = subprocess.check_output(
        ["ipconfig"],
        text=True
    )

    for line in output.splitlines():
        if "Default Gateway" in line:
            gateway = line.split(":")[-1].strip()

            if gateway:
                return gateway

    return "Not found"

def get_dns_server():
    output = subprocess.check_output(
        ["ipconfig", "/all"],
        text=True
    )

    for line in output.splitlines():
        if "DNS Servers" in line:
            dns = line.split(":")[-1].strip()

            if dns:
                return dns

    return "Not found"

def get_arp_table():
    output = subprocess.check_output(
        ["arp", "-a"],
        text=True
    )

    arp_entries = []

    for line in output.splitlines():
        parts = line.split()

        if len(parts) >= 3:
            ip = parts[0]
            mac = parts[1]
            entry_type = parts[2]

            try:
                ipaddress.IPv4Address(ip)

                arp_entries.append((ip, mac))

            except ipaddress.AddressValueError:
                continue

    return arp_entries


def get_listening_ports():
    output = subprocess.check_output(
        ["netstat", "-ano"],
        text=True
    )

    listening_ports = []

    for line in output.splitlines():
        parts = line.split()

        if len(parts) >= 5:
            protocol = parts[0]
            local_address = parts[1]
            state = parts[3]
            pid = parts[4]

            if protocol == "TCP" and state == "LISTENING":
                port = local_address.rsplit(":", 1)[-1]

                listening_ports.append((port, pid))



    return listening_ports

def test_connection(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)

        result = sock.connect_ex((target, port))

        sock.close()

        if result == 0:
            return "OPEN"
        else:
            return "CLOSED / UNREACHABLE"

    except socket.erro as error:
        return f"ERROR: {error}"


def get_network(ip, subnet_mask):
    network = ipaddress.IPv4Network(
        f"{ip}/{subnet_mask}",
        strict=False
    )

    return network


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