import tkinter as tk
from tkinter import messagebox

class GuessingGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Guessing Game")

        self.lower_bound = 1
        self.upper_bound = 100
        self.target_number = None

        self.label = tk.Label(root, text="Think of a number between 1 and 100 and I will guess it!")
        self.label.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Game", command=self.start_game)
        self.start_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

    def start_game(self):
        self.target_number = None
        self.lower_bound = 1
        self.upper_bound = 100
        self.result_label.config(text="")
        self.ask_guess()

    def ask_guess(self):
        if self.lower_bound > self.upper_bound:
            messagebox.showinfo("Oops!", "It seems you might have provided incorrect feedback.")
            return

        guess = (self.lower_bound + self.upper_bound) // 2
        response = messagebox.askyesno("Guess", f"Is your number {guess}?")

        if response:
            self.result_label.config(text=f"I guessed it! Your number was {guess}")
        else:
            response = messagebox.askyesno("Feedback", f"Is the number higher than {guess}? (Yes = Higher, No = Lower)")
            if response:
                self.lower_bound = guess + 1
                self.ask_guess()
            else:
                self.upper_bound = guess - 1
                self.ask_guess()

if __name__ == "__main__":
    root = tk.Tk()
    app = GuessingGameGUI(root)
    root.mainloop()
