import tkinter as tk

root = tk.Tk()
root.title("config windows")
root.geometry("300x600")

lab = tk.Label(root, text="라벨입니다.")
lab.pack()

btn = tk.Button(root, text="숫자를 올리자", command=doCount)


def doCount(num):
    num += 1
    lab.config(text="이번숫자는 {num} 입니다.")


root.mainloop()
