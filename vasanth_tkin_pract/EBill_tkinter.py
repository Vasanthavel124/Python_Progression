import tkinter as tk
from tkinter import messagebox
import random

class ElectricityBillGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Electricity Bill Management")

        self.cost_per_unit = 6.0

        self.customers = {
            101: {"name": "Alice", "units_consumed": random.randint(50, 500)},
            102: {"name": "Bob", "units_consumed": random.randint(50, 500)},
            # Add more customers as needed
        }

        self.label = tk.Label(root, text="Electricity Bill Management System")
        self.label.pack(pady=10)

        self.customer_id_label = tk.Label(root, text="Enter Customer ID:")
        self.customer_id_label.pack()

        self.customer_id_entry = tk.Entry(root)
        self.customer_id_entry.pack()

        self.show_details_button = tk.Button(root, text="Show Details", command=self.show_details)
        self.show_details_button.pack(pady=10)

        self.pay_button = tk.Button(root, text="Pay Bill", command=self.pay_bill, state=tk.DISABLED)
        self.pay_button.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def show_details(self):
        customer_id = int(self.customer_id_entry.get())
        if customer_id in self.customers:
            customer = self.customers[customer_id]
            units_consumed = customer["units_consumed"]
            name = customer["name"]
            bill_amount = units_consumed * self.cost_per_unit

            self.result_label.config(text=f"Name: {name}\nUnits Consumed: {units_consumed}\nBill Amount: {bill_amount:.2f} Rs")
            self.pay_button.config(state=tk.NORMAL)
        else:
            messagebox.showinfo("Error", "Customer not found.")

    def pay_bill(self):
        messagebox.showinfo("Payment", "Bill paid successfully!")
        self.pay_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = ElectricityBillGUI(root)
    root.mainloop()
