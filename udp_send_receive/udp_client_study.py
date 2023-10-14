import socket

udp_client_socket= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
port=1234
address = ('',port)

data="udp client 데이터입니다 "
udp_client_socket.sendto(data.encode(),('localhost',port))

