import socket

s_sock=socket.socket()
host = "localhost"

address=("locahost",5000)

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s_sock.connect(address)

print("I am ready")


fn=s_sock.recv(1024).decode()

with open ("./dummy"+"recv",'wb')as f:
    print("Receiving")
    while True:
        data=s_sock.recv(8192)
        if not data:
            break
        f.write(data)

print("Download complete")
s_sock.close()
