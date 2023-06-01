# 导入官方模块
import tkinter as tk
from tkinter import messagebox
import os
# 导入本地模块
import set_win_center

# 创建窗口：实例化一个窗口对象
root = tk.Tk()
# 窗口大小
set_win_center.set_win_center(root, 880, 540)
# 禁止窗口调整大小
root.resizable(width=False, height=False)
# 窗口标题
root.title("SuperHub")
# 窗口图标
root.iconbitmap("./logo.ico")

# --------------------------------主程序-----------------------------------


# -----------------------------------------------------------------------
# 显示窗口
root.mainloop()
