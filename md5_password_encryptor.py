import tkinter as tk
from tkinter import messagebox as msgbox
import hashlib


class Window(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title(" MD5 password ecryptor ")
        self.input_text = tk.StringVar()

        tk.Label(self,text=" Enter the text you want to hash in the md5 algo ").pack()
        tk.Entry(self, textvar=self.input_text).pack()
        tk.Button(self,text="submit", command=self.submit).pack()

    def submit(self):
        text = hashlib.md5(str(self.input_text.get()).encode()).hexdigest()
        msgbox.showinfo("Operation Succeded", f"result : \n {text}")

if __name__ == "__main__":
    Window().mainloop()