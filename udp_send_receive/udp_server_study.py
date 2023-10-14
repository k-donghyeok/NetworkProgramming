import socket
import random
udp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

if(udp_server_socket.bind(('',1234))==-1):
    print("서버 할당 실패")



str = "ACK"
while True:
    data, client_address = udp_server_socket.recvfrom(1024)
    if ((random.randint(1, 10) < 5)):
        print("송신실패")
        continue
    else:
        print(data.decode())
        udp_server_socket.sendto(str.encode(), client_address)




