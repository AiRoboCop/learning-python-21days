import tkinter as tk

# 창 만들기
root = tk.Tk()

# 창 제목 정하기
root.title("내 첫 GUI 프로그램")

# 창 크기 정하기(가로 * 세로, 픽셀)
root.geometry("400x300")

label = tk.Label(root, text="안녕하세요!")
label.pack()

button = tk.Button(root, text="클릭하세요")
button.pack()

# 창 유지하기(이게 없으면 바로 사라짐)
root.mainloop()
