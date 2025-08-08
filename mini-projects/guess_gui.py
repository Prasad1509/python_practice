import tkinter as tk
import random

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Guess the Number Game")
        self.root.geometry("400x300")
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.title_label = tk.Label(root, text="🔢 Guess the Number (1-100)", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        self.info_label = tk.Label(root, text="Enter your guess below:", font=("Arial", 12))
        self.info_label.pack()

        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=10)

        self.check_button = tk.Button(root, text="Check", command=self.check_guess, bg="#4CAF50", fg="white", font=("Arial", 12))
        self.check_button.pack()

        self.result_label = tk.Label(root, text="", font=("Arial", 12), fg="orange")
        self.result_label.pack(pady=10)

        self.reset_button = tk.Button(root, text="Reset Game", command=self.reset_game, bg="#f44336", fg="white", font=("Arial", 10))
        self.reset_button.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.secret_number:
                self.result_label.config(text="📉 Too low! Try again.")
            elif guess > self.secret_number:
                self.result_label.config(text="📈 Too high! Try again.")
            else:
                self.result_label.config(
                    text=f"🎉 Correct! You guessed it in {self.attempts} attempts.", fg="green"
                )
        except ValueError:
            self.result_label.config(text="⚠️ Please enter a valid number.", fg="red")

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="", fg="orange")

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
