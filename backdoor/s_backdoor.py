#!/usr/bin/env python
import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("192.168.8.145", 4444))
connection.send("\[+] Connection established.")
recieved_data = connection.recv(1024)
print(recieved_data)

connection.close()