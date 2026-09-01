import subprocess
import socket


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

    except socket.error as error:
        return f"ERROR: {error}"