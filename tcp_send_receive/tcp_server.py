import socket
import sys




c_sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address=('',5000)
c_sock.bind(address)

c_sock.listen(5)

msg =c_sock.recv(1024)
print(msg.decode())

client, addr=c_sock.accept()

if client:
    filename=client.send(input("파일이름을 입력하세요").encode())

with open("./dummy/" + filename,'rb') as f:
    c_sock.sendfile(f,0)

print('Sending complete')
c_sock.close()