import random
import socket
import cv2
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import threading


# 이미지 수신을 위한 소켓
image_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
image_client_address = ('localhost', 2500)
image_client_socket.connect(image_client_address)

# 텍스트 통신을 위한 소켓
text_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
text_client_address = ('localhost', 2501)
text_client_socket.connect(text_client_address)

root=tk.Tk()
label=tk.Label(root,text="클라이언트 화면")
label.pack()

text=tk.Text(root, wrap=tk.WORD, state=tk.DISABLED)
text.tag_configure("large_font", font=("Helvetica", 16))
text.pack()
entry=tk.Entry(root,width=40)
entry.pack()

class VideoThread(threading.Thread): #threading.Thread 클래스를 상속받는 VideoThread 클래스 정의
    def __init__(self): #클래스가 생성될떄 실행되는 생성자
        threading.Thread.__init__(self) # 부모클래스의 생성자 호출
    def run(self): #스레드가 시작될떄 실행되는 함수
        video_handler(image_client_socket) #실행되는 함수
class TextThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        receive_text(text_client_socket)

def video_handler(client_socket):
    while True:
        data = client_socket.recv(300000)  # 이미지 데이터 수신
        if not data:
            break

        frame_bytes = np.frombuffer(data, dtype=np.uint8)
        # NumPy 배열을 이미지로 디코딩
        if frame_bytes is not None:
            framedecode = cv2.imdecode(frame_bytes, cv2.IMREAD_COLOR)
            if framedecode is not None:
                # OpenCV 이미지를 Tkinter PhotoImage로 변환
                image = cv2.cvtColor(framedecode, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(image)
                photo = ImageTk.PhotoImage(image=image)

                label.config(image=photo)
                label.photo = photo
                root.update()
            else:
                print("framedecode 가없음")
        else:
            print("frame_bytes 가없음")


def send_text_handler():
    text=entry.get()
    text_client_socket.send(text.encode())
    print("텍스트 데이터 전송")
    entry.delete(0,tk.END)

def receive_text(client_socket):
    while True:
        data=client_socket.recv(1024)
        if data is not None:
            print("텍스트 데이터 수신",data.decode())

            text.config(state=tk.NORMAL)
            text.insert(1.0,data.decode()+"\n","large_font")
            text.config(state=tk.DISABLED)
            root.after(100,updategui)
        else:
            print("텍스트 데이터가 손실됨")
def updategui():
    print("asd")
    root.update()


btn_input=tk.Button(root,width=10,text="입력",overrelief='solid',command=send_text_handler)
btn_input.pack()

video_thread = VideoThread()
text_thread = TextThread()


video_thread.start()
text_thread.start()


root.mainloop()
