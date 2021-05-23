from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height = 0) #single:하나만 선택, extended:다중 선택. height =0이면 전체 보임.
listbox.insert(0, "딸기")
listbox.insert(1, "복숭아")
listbox.insert(2, "참외")
listbox.insert(END, "수박")
listbox.insert(END, "멜론")
listbox.pack()


def btncmd():
    #삭제
    # listbox.delete(END)

    #개수 확인
    # print("리스트에는", listbox.size(), "개가 있어요")

    #항목 확인(시작, 끝)
    # print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))

    #선택된  항목 확인(위치로 반환)
    # print("선택된 항목 : ", listbox.curselection())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()