import socket

udp_client_socket= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
port=1234
address = ('',port)

data="udp client 데이터입니다 "

for i in range(10):
    delay = 0.1
    while True:
        udp_client_socket.sendto(data.encode(), ('localhost', port))
        print('{} 시간동안 기다리겠습니다'.format(delay))
        udp_client_socket.settimeout(delay)
        try:
            recvdata, server_address = udp_client_socket.recvfrom(1024)
        except socket.timeout:
            delay *=2
            if delay >2.0:
                break
        else:
            print('클라이언트에서 수신한 데이터:',recvdata.decode())
            break

