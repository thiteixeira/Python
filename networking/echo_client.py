#!/usr/bin/env python
# echo_client.py

import socket

host = socket.gethostname()
port = 12345 # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print('Sending Hello, world')
s.sendall('Hello, world'.encode())
data = s.recv(1024)
s.close()
print('Received', repr(data))
