import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
import pytesseract

root = tk.Tk()


class ExtractedData:
    def __init__(self, text=''):
        self._text = text

    # getter method
    def get_text(self):
        return self._text

    # setter method
    def set_text(self, x):
        self._text = x

    text = property(get_text, set_text)


def get_Image(tk_textbox):
    try:
        # Clear textbox and initialize a new ExtractedData object to send text to
        tk_textbox.delete('1.0', tk.END)
        newExtraction = ExtractedData
        # Browse local files & get path
        file_path = filedialog.askopenfilename(parent=root, initialdir='/', initialfile='tmp',
                                               filetypes=[("All files", "*")])

        # Convert image to text with ocr-tesseract
        img = cv2.imread(file_path)
        newExtraction.text = pytesseract.image_to_string(img, lang="eng")
        tk_textbox.insert(tk.END, ExtractedData.text)
    except (ValueError, Exception):
        tk.messagebox.showerror('Upload Error', 'Image not uploaded. Please try again.')
        pass


def save_txt_file():

    folder_path = filedialog.askdirectory()
    if not folder_path:
        tk.messagebox.showerror('Save Error', 'Text not saved. Please select a path to save the file.')
    elif ExtractedData.text != '':
        tk.messagebox.showerror('Save Error', 'Text not saved. '
                                              'First, you need to use the browse button to extract the text.')
    else:
        with open(folder_path+"/Output.txt", "w") as text_file:
            text_file.write(str(ExtractedData.text))


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
    browse_button.place(relx=0.25, rely=0.2, anchor=tk.CENTER)

    exit_button = tk.Button(root, text="Exit", fg="red", command=lambda: root.quit())
    exit_button.pack(side=tk.RIGHT, ipadx=5, ipady=5, expand=True)
    exit_button.place(relx=0.72, rely=0.2, anchor=tk.CENTER)

    save_button = tk.Button(root, text="Save .txt file", fg="green", command=lambda: save_txt_file())
    save_button.pack(side=tk.RIGHT, ipadx=5, ipady=5, expand=True)
    save_button.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    root.mainloop()


if __name__ == '__main__':
    start_UI()
