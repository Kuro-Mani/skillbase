import csv
import random
import tkinter as tk
from tkinter import messagebox

class CSVToolGUI:
    def __init__(self, master, csv_file):
        self.master = master
        self.csv_file = csv_file
        self.remaining_items = []

        self.master.title("CSV Tool")

        self.label = tk.Label(master, text="What does the word mean?", font=("Arial", 16))
        self.label.pack()

        self.item_var = tk.StringVar()
        self.item_label = tk.Label(master, textvariable=self.item_var, font=("Arial", 14))
        self.item_label.pack()

        self.input_label = tk.Label(master, text="Enter an item:", font=("Arial", 14))
        self.input_label.pack()

        self.user_input = tk.Entry(master, font=("Arial", 14))
        self.user_input.pack()

        self.check_button = tk.Button(master, text="Check", command=self.check_input, font=("Arial", 14))
        self.check_button.pack()

        self.result_label = tk.Label(master, text="", font=("Arial", 14))
        self.result_label.pack()

        self.quit_button = tk.Button(master, text="Quit", command=master.quit, font=("Arial", 14))
        self.quit_button.pack()

        self.load_csv()
        self.display_next_item()

    def load_csv(self):
        try:
            with open(self.csv_file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader) 
                self.remaining_items = list(reader)
        except FileNotFoundError:
            messagebox.showerror("Error", "CSV file not found.")

    def display_next_item(self):
        if self.remaining_items:
            random_row = random.choice(self.remaining_items)
            self.item_var.set(random_row[0])
            self.current_row = random_row
        else:
            self.result_label.config(text="Congratulations!")
            self.check_button.config(state=tk.DISABLED)

    def check_input(self):
        user_input = self.user_input.get()
        if user_input == self.current_row[1]:
            self.result_label.config(text="Match! The word is: {}".format(self.current_row[1]))
            self.remaining_items.remove(self.current_row)
        else:
            self.result_label.config(text="No match. The correct word is: {}".format(self.current_row[1]))

        self.display_next_item()

if __name__ == "__main__":
    csv_file = "data.csv"
    root = tk.Tk()
    app = CSVToolGUI(root, csv_file)
    root.mainloop()
