import socket

tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port=1024
ip=''
address=(ip,port)
if(tcp_server_socket.bind(address)==-1):
    print("서버 할당실패")
else:
    print("서버 할당성공")

tcp_server_socket.listen(1)

client_socket,clinet_address =tcp_server_socket.accept()

data=client_socket.recv(1024)
if(data==-1):
    print("수신실패")

print("서버에서 수신한 데이터: ",data.decode())



