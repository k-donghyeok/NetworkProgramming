import socket
import cv2
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import threading

# 이미지 수신을 위한 소켓
image_client_sockets = []
text_client_sockets = []

image_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #이미지 수신을 위한 소켓 생성 ipv4 주소형식,tcp 소켓 사용
image_server_ip = '' # 모든 사용가능한 인터페이스 바인딩을 위한 ip 주소
image_server_port = 2500 # 포트번호
image_server_socket.bind((image_server_ip, image_server_port)) #소켓에 주소와 포트번호 할당
image_server_socket.listen(5) # 클라이언트가 해당소켓에 연결 요청을 하러왔을때 대기할수있는 대기열 생성

text_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
text_server_ip = ''
text_server_port = 2501
text_server_socket.bind((text_server_ip, text_server_port))
text_server_socket.listen(5)

root = tk.Tk()
label = tk.Label(root, text="서버 화면")
label.pack()

text = tk.Text(root, wrap=tk.WORD, width=40, height=10, state=tk.DISABLED)
text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


def accept_connections():
    while True:
        image_socket, _ = image_server_socket.accept() # 해당소켓에 연결요청 이 올때까지 대기하다가 요청이오면 클라이언트 소켓과 주소 반환
        text_socket, _ = text_server_socket.accept()
        image_client_sockets.append(image_socket)
        text_client_sockets.append(text_socket)
        image_thread = threading.Thread(target=video_handler) # target= 뒤에적힌 함수를 실행하는 스레드 생성 args= 뒤에 함수에서 사용할 매개변수 지정해줄수있음
        image_thread.start()# 스레드 시작
        text_thread = threading.Thread(target=receieve_send_text, args=(text_socket,))
        text_thread.start()

def video_handler():
    video = cv2.VideoCapture(0)
    if not video.isOpened():
        print("웹캠을 열 수 없습니다")
        return

    while True:
        ret, frame = video.read()
        if ret:
            _, encodeframe = cv2.imencode(".jpg", frame)
            encodeframe_byte = encodeframe.tobytes()

            for sock in image_client_sockets:
                sock.sendall(encodeframe_byte)
        else:
            print("웹캠 정보를 읽어오는데 문제가 있음")

def receieve_send_text(text_socket):
    while True:
        data = text_socket.recv(1024) # 해당소켓을 이용해 수신한 데이터를 받아서 저장 한번에 최대 1024 바이트 크기 읽을수있음
        if data:
            for sock in text_client_sockets:
                sock.send(data) # 연결된 클라이언트 소켓으로 데이터 송신

accept_thread = threading.Thread(target=accept_connections)
accept_thread.start()


root.mainloop()
