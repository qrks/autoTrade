#coding:utf-8

import socket

remote_host = '127.0.0.1'
remote_port = 9999
send_buf = 'test text' 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((remote_host, remote_port))
sock.send(send_buf)
response_data = sock.recv(1024)
print response_data
sock.close(  )