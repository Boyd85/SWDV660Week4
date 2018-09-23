import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 9500        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    data = conn.recv(1024).decode()
    with conn:
        print('Connected by', addr)    
        if data == 'Hello':
            conn.send('Hi'.encode())
        else:
            conn.send('Goodbye'.encode())
