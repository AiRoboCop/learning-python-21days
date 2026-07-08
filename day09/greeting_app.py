import tkinter as tk


def say_hello():
    name = entry.get()
    result_label.config(text=f"안녕하세요, {name}님!")


root = tk.Tk()
root.title("인사프로그램")
root.geometry("400x300")

guide_label = tk.Label(root, text="이름을 입력하세요")
guide_label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="인사하기", command=say_hello)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
