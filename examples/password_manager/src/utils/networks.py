from socket import socket


def find_available_port():
    with socket() as s:
        s.bind(("", 0))
        return s.getsockname()[1]
