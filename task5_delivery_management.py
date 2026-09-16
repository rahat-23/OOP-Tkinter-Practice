import tkinter as tk
from tkinter import ttk


# Parent Class
class Delivery:
    def __init__(self, order_id, destination):
        self.order_id = order_id
        self.destination = destination

    def deliver(self):
        return f"Delivering order {self.order_id}"


# Second Parent Class
class Trackable:
    def track(self):
        return f"Tracking order {self.order_id}..."


# Child Class 1
class StandardDelivery(Delivery):
    def deliver(self):
        return (
            f"Order {self.order_id} will arrive at "
            f"{self.destination} in 3-5 days."
        )


# Child Class 2
class ExpressDelivery(Delivery, Trackable):
    def deliver(self):
        return (
            f"Order {self.order_id} will arrive at "
            f"{self.destination} within 24 hours."
        )


# GUI Function
def create_delivery():
    order_id = order_entry.get()
    destination = destination_entry.get()
    selected_type = delivery_type.get()

    if selected_type == "Standard":
        delivery = StandardDelivery(order_id, destination)

    else:
        delivery = ExpressDelivery(order_id, destination)

    # Polymorphism
    result_label.config(text=delivery.deliver())

    # Save current object for tracking
    current_delivery["object"] = delivery


def track_delivery():
    delivery = current_delivery["object"]

    if delivery is None:
        result_label.config(text="Please create a delivery first.")
        return

    if isinstance(delivery, ExpressDelivery):
        result_label.config(
            text=f"{delivery.deliver()}\n{delivery.track()}"
        )
    else:
        result_label.config(
            text="Tracking is available only for Express Delivery."
        )


# Main Window
root = tk.Tk()
root.title("Delivery Management System")
root.geometry("500x430")


# Dictionary to store current delivery object
current_delivery = {"object": None}


# Title
title_label = tk.Label(
    root,
    text="Delivery Management System",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=20)


# Order ID
tk.Label(root, text="Enter Order ID:").pack()

order_entry = tk.Entry(root, width=30)
order_entry.pack(pady=5)


# Destination
tk.Label(root, text="Enter Destination:").pack()

destination_entry = tk.Entry(root, width=30)
destination_entry.pack(pady=5)


# Delivery Type
tk.Label(root, text="Select Delivery Type:").pack()

delivery_type = ttk.Combobox(
    root,
    values=["Standard", "Express"],
    state="readonly"
)

delivery_type.set("Standard")
delivery_type.pack(pady=5)


# Create Delivery Button
create_button = tk.Button(
    root,
    text="Create Delivery",
    command=create_delivery
)

create_button.pack(pady=10)


# Track Button
track_button = tk.Button(
    root,
    text="Track Delivery",
    command=track_delivery
)

track_button.pack(pady=10)


# Result
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12)
)

result_label.pack(pady=20)


root.mainloop()