import socket
import cv2
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import threading

# 이미지 수신을 위한 소켓
image_client_sockets = []
text_client_sockets = []

image_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
image_server_ip = ''
image_server_port = 2500
image_server_socket.bind((image_server_ip, image_server_port))
image_server_socket.listen(5)

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
        image_socket, _ = image_server_socket.accept()
        text_socket, _ = text_server_socket.accept()
        image_client_sockets.append(image_socket)
        text_client_sockets.append(text_socket)
        image_thread = threading.Thread(target=video_handler)
        image_thread.start()
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
        data = text_socket.recv(1024)
        if data:
            for sock in text_client_sockets:
                sock.send(data)

accept_thread = threading.Thread(target=accept_connections)
accept_thread.start()


root.mainloop()
