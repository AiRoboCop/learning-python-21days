import tkinter as tk

root = tk.Tk()

root.title("pack side 테스트")
root.geometry("400x300")

tk.Label(root, text="left_1", bg="lightblue").pack(expand=True, fill="y")
# tk.Label(root, text="left_2", bg="lightgreen").pack(fill="x")
# tk.Label(root, text="left_3", bg="lightyellow").pack(side="right")


root.mainloop()
