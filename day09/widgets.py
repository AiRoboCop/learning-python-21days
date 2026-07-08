import tkinter as tk

root = tk.Tk()
root.title("위젯 연습")
root.geometry("400x300")

label = tk.Label(
    root,
    text="안녕하세요, 윤종님",
    font=("맑은 고딕", 20),
    fg="blue",
    bg="yellow",
)
label.pack(padx=10)

label2 = tk.Label(root, text="GUI 프로구래밍 첫날이군요")
label2.pack()

button = tk.Button(root, text="클릭하세요")
button.pack()

entry = tk.Entry(root)
entry.pack()

name = entry.get()


def say_hello():
    print("버튼이 눌렸어요!")


button = tk.Button(root, text="클릭", command=say_hello)
button.pack()

root.mainloop()
