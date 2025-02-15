import tkinter as tk
from tkinter import messagebox
import json
import os

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        
        # Initialize data storage
        self.expenses = {}
        self.load_data()

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        # Labels
        tk.Label(self.root, text="Expense Amount (INR):").grid(row=0, column=0)
        tk.Label(self.root, text="Category:").grid(row=1, column=0)

        # Entry fields
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.grid(row=0, column=1)

        self.category_entry = tk.Entry(self.root)
        self.category_entry.grid(row=1, column=1)

        # Add Expense Button
        self.add_button = tk.Button(self.root, text="Add Expense", command=self.add_expense)
        self.add_button.grid(row=2, column=0, columnspan=2)

        # Summary Button
        self.summary_button = tk.Button(self.root, text="Show Summary", command=self.show_summary)
        self.summary_button.grid(row=3, column=0, columnspan=2)

    def add_expense(self):
        try:
            amount = float(self.amount_entry.get())
            category = self.category_entry.get().strip()

            if category == "":
                messagebox.showerror("Input Error", "Category cannot be empty.")
                return

            # Store the expense
            if category in self.expenses:
                self.expenses[category] += amount
            else:
                self.expenses[category] = amount

            # Clear the entry fields
            self.amount_entry.delete(0, tk.END)
            self.category_entry.delete(0, tk.END)

            # Save data to file
            self.save_data()

            messagebox.showinfo("Success", "Expense added successfully!")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid amount.")

    def show_summary(self):
        total = sum(self.expenses.values())
        average = total / len(self.expenses) if self.expenses else 0
        summary = f"Total Expenses: ₹{total:.2f}\nAverage Expense: ₹{average:.2f}\n\nBreakdown:\n"

        for category, amount in self.expenses.items():
            summary += f"{category}: ₹{amount:.2f}\n"

        messagebox.showinfo("Expense Summary", summary)

    def save_data(self):
        with open("expenses.json", "w") as f:
            json.dump(self.expenses, f)

    def load_data(self):
        if os.path.exists("expenses.json"):
            with open("expenses.json", "r") as f:
                self.expenses = json.load(f)

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()