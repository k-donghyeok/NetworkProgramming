import tkinter
from tkinter import *

def cal_plus():
    num1=int(entry1.get())
    num2=int(entry2.get())
    label.config(text=str(num1+num2))
    text.insert(tkinter.END,str(num1+num2)+"\n","large_font")
    root.after(100,udp)
def udp():
    root.update()

root = Tk()
root.title("opt window")
root.geometry("300x200+300+300")
root.resizable(False,False)

label=Label(root,text="결과값")
label.pack()

entry1=Entry(root,width=15)
entry1.pack()
entry2=Entry(root,width=15)
entry2.pack()

button=Button(root,width=10,text="더하기",overrelief="solid",command=cal_plus)
button.pack()

text=tkinter.Text(root,width=40,height=10,state=tkinter.DISABLED)
text.tag_configure("large_font", font=("Helvetica", 16))
text.pack()

root.mainloop()
