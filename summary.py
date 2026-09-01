import json


with open("network.json", "r") as file:
    data = json.load(file)


print("==============================")
print("       NETWORK SUMMARY")
print("==============================")

print()
print("Hostname:", data["hostname"])
print("IPv4 Address:", data["ipv4_address"])
print("Subnet Mask:", data["subnet_mask"])
print("Default Gateway:", data["default_gateway"])
print("DNS Server:", data["dns_server"])
print("ARP Table:")
for ip, mac in data["arp_table"]:
    print(f"  {ip}:          {mac}")


print()
print("Listening Ports:")

for port in data["listening_ports"]:
    print(port)

