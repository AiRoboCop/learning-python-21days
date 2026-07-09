import tkinter as tk

num = 0


def doCount():
    global num
    num += 1
    lab.config(text=f"이번숫자는 {num} 입니다.")


root = tk.Tk()
root.title("config windows")
root.geometry("300x600")

lab = tk.Label(root, text="라벨입니다.")
lab.pack()

btn = tk.Button(root, text="숫자를 올리자", command=doCount)
btn.pack(pady=20)

root.mainloop()
