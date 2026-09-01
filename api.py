from fastapi import FastAPI
from system import get_hostname
from network import get_arp_table, get_dns_server, get_ipv4, get_network, get_subnet_mask, get_default_gateway
from ports import get_listening_ports, test_connection

app = FastAPI(
    title="Network Detective API",
    description="Security-oriented backend for investigating your own machine",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Network Detective API is running"
    }


@app.get("/system")
def system_info():
    return {
        "hostname": get_hostname()
    }


@app.get("/network")
def network_info():
    return {
        "ip_address": get_ipv4(),
        "subnet_mask": get_subnet_mask(),
        "default_gateway": get_default_gateway(),
        "dns_server": get_dns_server(),
        "arp_table": get_arp_table(),
        "network": get_network(get_ipv4(), get_subnet_mask())
    }


@app.get("/ports")
def ports_info():
    return {
        "listening_ports": get_listening_ports()
    }


@app.get("/test-connection")
def connection_test(target: str, port: int):
    status = test_connection(target, port)

    return {
        "target": target,
        "port": port,
        "status": status
    }