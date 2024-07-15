"""Simple guess the number game"""

import random

from tkinter import messagebox, Tk, Entry, Button, Label, DISABLED


def generate_random_list():
    """Generates a random list of 10 numbers"""
    start = random.randint(1, 91)
    random_number_list = list(range(start, start + 10))
    return random_number_list


def get_random_number(list_of_numbers):
    """Selects a random number from the given list"""
    random_number = random.choice(list_of_numbers)
    return list_of_numbers, random_number


def start_game():
    """Start guessing game with Tkinter interface"""
    list_of_numbers = generate_random_list()
    list_of_numbers, random_number = get_random_number(list_of_numbers)

    attempts = 3

    def check_guess():
        nonlocal attempts
        try:
            guess = int(entry_guess.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return

        if guess == random_number:
            messagebox.showinfo("Result", "You guessed right!")
        else:
            attempts -= 1
            if attempts > 0:
                if guess > random_number:
                    messagebox.showinfo("Result", "Guess lower.")
                else:
                    messagebox.showinfo("Result", "Guess higher.")
                label_attempts.config(text=f"You have {attempts} attempts left.")

            else:
                messagebox.showinfo(
                    "Result",
                    f"Better luck next time! I was thinking about {random_number}.",
                )
                button_check.config(state=DISABLED)

    # Create the main window
    root = Tk()
    root.title("Guess the Number")

    # Create and place the widgets
    Label(
        root,
        text=f"I'm thinking of a number between {list_of_numbers[0]} and {list_of_numbers[-1]}.",
    ).pack(pady=10)
    Label(root, text="What number am I thinking?").pack()

    entry_guess = Entry(root)
    entry_guess.pack(pady=5)

    button_check = Button(root, text="Check Guess", command=check_guess)
    button_check.pack(pady=5)

    label_attempts = Label(root, text=f"You have {attempts} attempts left.")
    label_attempts.pack(pady=10)

    # Start the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    start_game()
