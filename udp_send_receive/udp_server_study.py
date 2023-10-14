import socket

udp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

if(udp_server_socket.bind(('',1234))==-1):
    print("서버 할당 실패")

data,client_address =udp_server_socket.recvfrom(1024)

print(data.decode())


