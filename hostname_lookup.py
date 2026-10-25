import socket

hostname = "localhost"
ip_address = socket.gethostbyname(hostname)

print(f"Hello! The IP address of {hostname} is {ip_address}.")