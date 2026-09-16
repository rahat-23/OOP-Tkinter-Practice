import tkinter as tk


# Parent Class
class Notification:
    def __init__(self, recipient):
        self.recipient = recipient

    def send(self):
        return "Sending notification..."


# Child Class 1
class EmailNotification(Notification):
    def send(self):
        return f"Sending Email to {self.recipient}"


# Child Class 2
class SMSNotification(Notification):
    def send(self):
        return f"Sending SMS to {self.recipient}"


# GUI Function
def send_notification():
    recipient = entry.get()

    email = EmailNotification(recipient)
    result_label.config(text=email.send())


# Main Window
root = tk.Tk()
root.title("Notification System")
root.geometry("400x250")

title = tk.Label(
    root,
    text="Notification System",
    font=("Arial", 18, "bold")
)
title.pack(pady=20)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

send_button = tk.Button(
    root,
    text="Send Email",
    command=send_notification
)
send_button.pack(pady=10)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12)
)
result_label.pack(pady=20)

root.mainloop()