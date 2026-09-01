import socket
import subprocess
import ipaddress

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

def get_network(ip, subnet_mask):
    network = ipaddress.IPv4Network(
        f"{ip}/{subnet_mask}",
        strict=False
    )

    return network