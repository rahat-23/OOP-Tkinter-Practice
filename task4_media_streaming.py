import tkinter as tk
from tkinter import ttk


# Parent Class
class Media:
    def __init__(self, title):
        self.title = title

    def play(self):
        return f"Playing media: {self.title}"


# Child Class
class Audio(Media):
    def __init__(self, title, duration):
        super().__init__(title)
        self.duration = duration

    def play(self):
        return f"Playing audio: {self.title} - {self.duration} minutes"


# Grandchild Class
class Podcast(Audio):
    def __init__(self, title, duration, host):
        super().__init__(title, duration)
        self.host = host

    def play(self):
        return f"Playing podcast: {self.title} hosted by {self.host}"


# GUI Function
def play_media():
    title = title_entry.get()
    duration = duration_entry.get()
    host = host_entry.get()

    selected_type = media_type.get()

    if selected_type == "Media":
        media_object = Media(title)

    elif selected_type == "Audio":
        media_object = Audio(title, duration)

    else:
        media_object = Podcast(title, duration, host)

    # Polymorphism
    result_label.config(text=media_object.play())


# Main Window
root = tk.Tk()
root.title("Media Streaming System")
root.geometry("500x450")


# Title
title_label = tk.Label(
    root,
    text="Media Streaming System",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=20)


# Media Type
tk.Label(root, text="Select Media Type:").pack()

media_type = ttk.Combobox(
    root,
    values=["Media", "Audio", "Podcast"],
    state="readonly"
)

media_type.set("Media")
media_type.pack(pady=5)


# Title
tk.Label(root, text="Enter Title:").pack()

title_entry = tk.Entry(root, width=30)
title_entry.pack(pady=5)


# Duration
tk.Label(root, text="Enter Duration (minutes):").pack()

duration_entry = tk.Entry(root, width=30)
duration_entry.pack(pady=5)


# Host
tk.Label(root, text="Enter Host Name:").pack()

host_entry = tk.Entry(root, width=30)
host_entry.pack(pady=5)


# Button
play_button = tk.Button(
    root,
    text="Play Media",
    command=play_media
)

play_button.pack(pady=15)


# Result
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12)
)

result_label.pack(pady=20)


root.mainloop()