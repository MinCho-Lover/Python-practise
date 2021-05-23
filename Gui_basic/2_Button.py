from tkinter import *

root = Tk()
root.title("Nado GUI")

btn1 = Button(root, text="버튼1")
btn1.pack() #화면에 버튼을 포함

btn2 = Button(root, padx=5, pady=10, text="버튼2") #pad는 버튼 내부 여백
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼2")
btn3.pack()

btn4 = Button(root, fg="red", bg="yellow", text="버튼4")
btn4.pack()

def btncmd():
    print("버튼이 클릭됐습니다.")
btn5 = Button(root, text="동작하는 버튼", command=btncmd)
btn5.pack()

root.mainloop()