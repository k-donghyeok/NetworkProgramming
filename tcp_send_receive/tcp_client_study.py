import socket

tcp_clinet_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=1024

tcp_clinet_socket.connect(('localhost',port))

data="hello"

tcp_clinet_socket.send(data.encode())

