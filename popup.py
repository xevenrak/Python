import tkinter as tk
from tkinter import messagebox

def show_popup():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo("warning", "i'm inside your walls.")
    root.mainloop()

show_popup()
