#!/usr/bin/env python3
import socket
import time

IP = '0.0.0.0'
PORT = 5000
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
s.listen(1)

while True:
	conn, addr = s.accept()
	data = conn.recv(BUFFER_SIZE)
	if not data:
		continue
	print('Alice says "{}"'.format(data.decode('utf8')))
	#conn.send(data)
	conn.close()