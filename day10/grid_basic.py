import tkinter as tk

root = tk.Tk()
root.title("Gird 테스트")
root.geometry("300x300")

label = tk.Label(root, text="gride위의 label입니다.")
entry = tk.Entry(root, background="yellow")

label.grid(row=0, column=0)
entry.grid(row=1, column=1)


root.mainloop()
