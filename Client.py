import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 9500        # The port used by the server

message = 'Hello'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(message.encode())
    data = s.recv(1024)

print(repr(data.decode()))