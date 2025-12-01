import tkinter as tk


def on_click():
    label.config(text="你按下了按鈕！")


# 建立主視窗
root = tk.Tk()
root.title("我的 GUI 範例")

# 建立標籤
label = tk.Label(root, text="Hello, GUI!")
label.pack()

# 建立按鈕
button = tk.Button(root, text="點我", command=on_click)
button.pack()

# 啟動事件迴圈
root.mainloop()
