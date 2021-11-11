import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import cv2
import pytesseract

root = tk.Tk()
root.withdraw()
style = ttk.Style(root)
style.theme_use("clam")


def get_Image():
    # Browse local files & get path
    file_path = filedialog.askopenfilename(parent=root, initialdir='/', initialfile='tmp',
                                           filetypes=[("All files", "*")])

    # Convert image to text with tesseract
    img = cv2.imread(file_path)
    text = pytesseract.image_to_string(img, lang="eng")
    print(text)


if __name__ == '__main__':
    get_Image()
