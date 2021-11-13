import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import cv2
import pytesseract

root = tk.Tk()

def get_Image(tk_text):
    # Browse local files & get path
    file_path = filedialog.askopenfilename(parent=root, initialdir='/', initialfile='tmp',
                                           filetypes=[("All files", "*")])

    # Convert image to text with tesseract
    img = cv2.imread(file_path)
    text = pytesseract.image_to_string(img, lang="eng")
    tk_text.insert(tk.END, text)


def start_UI():
    # GUI
    root.geometry('300x500')
    root.resizable(False, False)
    root.title('Image2Text')
    var = tk.StringVar()
    welcome_msg = "Welcome! " \
                  "\n\nExtract text from image -> download as .txt file." \
                  "\n-TO START CLICK ON BROWSE- "
    var.set(welcome_msg)
    title = tk.Label(root, textvariable=var)
    title.pack()
    # Text box location to set the extracted text
    text_entry = tk.Text(root, width=30, height=25)
    text_entry.place(relx=0.5, rely=1.1, anchor=tk.S)
    # Buttons
    browse_button = tk.Button(root, text='Browse', command=lambda: get_Image(text_entry))
    browse_button.pack(side=tk.LEFT, ipadx=5, ipady=5, expand=True)
    browse_button.place(relx=0.3, rely=0.2, anchor=tk.CENTER)

    exit_button = tk.Button(root, text="Exit", fg="red", command=lambda: root.quit())
    exit_button.pack(side=tk.RIGHT, ipadx=5, ipady=5, expand=True)
    exit_button.place(relx=0.7, rely=0.2, anchor=tk.CENTER)
    root.mainloop()


if __name__ == '__main__':
    start_UI()


