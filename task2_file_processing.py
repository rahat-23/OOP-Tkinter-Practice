import tkinter as tk
from tkinter import ttk


# Parent Class
class FileProcessor:
    def __init__(self, filename):
        self.filename = filename

    def process(self):
        return "Processing file..."


# Child Class 1
class TextFile(FileProcessor):
    def process(self):
        return f"Processing text file: {self.filename}"


# Child Class 2
class ImageFile(FileProcessor):
    def process(self):
        return f"Processing image file: {self.filename}"


# Child Class 3
class AudioFile(FileProcessor):
    def process(self):
        return f"Processing audio file: {self.filename}"


# GUI Function
def process_file():
    filename = filename_entry.get()

    selected_type = file_type.get()

    if selected_type == "Text":
        file_object = TextFile(filename)

    elif selected_type == "Image":
        file_object = ImageFile(filename)

    else:
        file_object = AudioFile(filename)

    # Polymorphism
    result_label.config(text=file_object.process())


# Main Window
root = tk.Tk()
root.title("File Processing System")
root.geometry("450x350")


# Title
title = tk.Label(
    root,
    text="File Processing System",
    font=("Arial", 18, "bold")
)
title.pack(pady=20)


# File Name
tk.Label(
    root,
    text="Enter File Name:"
).pack()

filename_entry = tk.Entry(
    root,
    width=30
)
filename_entry.pack(pady=10)


# File Type
tk.Label(
    root,
    text="Select File Type:"
).pack()

file_type = ttk.Combobox(
    root,
    values=["Text", "Image", "Audio"],
    state="readonly"
)

file_type.set("Text")
file_type.pack(pady=10)


# Button
process_button = tk.Button(
    root,
    text="Process File",
    command=process_file
)

process_button.pack(pady=15)


# Result
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12)
)

result_label.pack(pady=20)


root.mainloop()