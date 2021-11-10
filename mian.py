import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import os

root = tk.Tk()
root.withdraw()
style = ttk.Style(root)
style.theme_use("clam")


def get_Image():
    file = filedialog.askopenfilenames(parent=root, initialdir='/', initialfile='tmp',
                                       filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("All files", "*")])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_Image()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
