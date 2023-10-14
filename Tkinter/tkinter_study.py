

from tkinter import *

def cal_plus():
    num1=int(entry1.get())
    num2=int(entry2.get())
    label.config(text=str(num1+num2))

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
root.mainloop()
