#!/usr/bin/env python3
import socket
import time

IP = '192.168.0.3'
PORT = 5000
BUFFER_SIZE = 1024
MESSAGE = b'Hello, World!'

while True:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((IP, PORT))
	s.sendall(MESSAGE)
	data = s.recv(BUFFER_SIZE)
	s.close()
	#print("Received data:", data)
	time.sleep(1)