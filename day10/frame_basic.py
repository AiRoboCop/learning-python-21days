import tkinter as tk

root = tk.Tk()
root.title("Frame 연습")
root.geometry("400x300")

top_frame = tk.Frame(root, bg="lightblue", height=100)
top_frame.pack(fill="x", padx=10, pady=10)

tk.Label(top_frame, text="상단영역", bg="lightblue").pack()
tk.Button(top_frame, text="버튼 A").pack(side="left", padx=5)
tk.Button(top_frame, text="버튼 B").pack(side="left", padx=5)

bottom_frame = tk.Frame(root, bg="lightgreen", height=100)
bottom_frame.pack(fill="x", padx=10, pady=10)

tk.Label(bottom_frame, text="하단영역", bg="lightgreen").pack()
tk.Button(bottom_frame, text="버튼 C").pack(side="left", padx=5)


root.mainloop()
