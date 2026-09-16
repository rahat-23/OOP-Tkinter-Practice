import tkinter as tk
from tkinter import ttk


# Parent Class
class Staff:
    def __init__(self, name, staff_id):
        self.name = name
        self.staff_id = staff_id

    def work(self):
        return f"{self.name} is working."


# Child Class 1
class Doctor(Staff):
    def __init__(self, name, staff_id, specialization):
        super().__init__(name, staff_id)
        self.specialization = specialization

    def work(self):
        return f"Dr. {self.name} is examining patients."


# Child Class 2
class Nurse(Staff):
    def __init__(self, name, staff_id, ward):
        super().__init__(name, staff_id)
        self.ward = ward

    def work(self):
        return f"Nurse {self.name} is caring for patients."


# Child Class 3
class Receptionist(Staff):
    def __init__(self, name, staff_id, shift):
        super().__init__(name, staff_id)
        self.shift = shift

    def work(self):
        return f"{self.name} is managing appointments."


# GUI Function
def show_work():
    name = name_entry.get()
    staff_id = id_entry.get()
    detail = detail_entry.get()
    selected_role = role.get()

    if selected_role == "Doctor":
        staff_member = Doctor(name, staff_id, detail)
        extra_info = f"Specialization: {staff_member.specialization}"

    elif selected_role == "Nurse":
        staff_member = Nurse(name, staff_id, detail)
        extra_info = f"Ward: {staff_member.ward}"

    else:
        staff_member = Receptionist(name, staff_id, detail)
        extra_info = f"Shift: {staff_member.shift}"

    result_label.config(
        text=f"Staff ID: {staff_member.staff_id}\n"
             f"{extra_info}\n"
             f"{staff_member.work()}"
    )


# Main Window
root = tk.Tk()
root.title("Hospital Staff Management")
root.geometry("500x450")


# Title
title = tk.Label(
    root,
    text="Hospital Staff Management",
    font=("Arial", 18, "bold")
)
title.pack(pady=20)


# Name
tk.Label(root, text="Enter Name:").pack()

name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)


# Staff ID
tk.Label(root, text="Enter Staff ID:").pack()

id_entry = tk.Entry(root, width=30)
id_entry.pack(pady=5)


# Role
tk.Label(root, text="Select Role:").pack()

role = ttk.Combobox(
    root,
    values=["Doctor", "Nurse", "Receptionist"],
    state="readonly"
)
role.set("Doctor")
role.pack(pady=5)


# Special Detail
tk.Label(
    root,
    text="Enter Specialization / Ward / Shift:"
).pack()

detail_entry = tk.Entry(root, width=30)
detail_entry.pack(pady=5)


# Button
show_button = tk.Button(
    root,
    text="Show Work",
    command=show_work
)
show_button.pack(pady=15)


# Result
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12)
)
result_label.pack(pady=20)


root.mainloop()