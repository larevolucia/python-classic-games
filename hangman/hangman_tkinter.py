"""Hangman game using tkinter"""

import random

from tkinter import Tk, Label, simpledialog, messagebox

# from PIL import Image, ImageTk


def select_word():
    """Select a random word from a list of possible words."""
    words = ["parachute", "trailblazer", "sparrow", "canine", "freight", "patronize"]
    return random.choice(words)


def initialize_game(word):
    """Initialize game variables."""
    guess_left = 7
    guess_progress = "*" * len(word)
    guessed_letters = []
    return guess_left, guess_progress, guessed_letters


def get_guess(guessed_letters):
    """Get a valid guess from the player."""
    while True:
        key = simpledialog.askstring("Guess", "Guess a letter: ")
        if key.isalpha() and len(key) == 1:
            if key not in guessed_letters:
                return key
            else:
                messagebox.showinfo("Invalid guess", "You tried that letter already!")
        else:
            messagebox.showinfo(
                "Invalid guess", "Please enter a single alphabetic character."
            )


def update_progress(word, guess_progress, key):
    """Update the guess progress with the guessed letter."""
    new_guess_progress = list(guess_progress)
    for i, letter in enumerate(word):
        if letter == key:
            new_guess_progress[i] = key
    return "".join(new_guess_progress)


def check_game_over(word, guess_progress, guess_left):
    """Check if the game is over (win or lose)."""
    if "*" not in guess_progress:
        messagebox.showinfo("Congratulations", "You win! The word was: " + word)
        return True
    if guess_left == 0:
        messagebox.showinfo("Game over", "You lose! The word was " + word)
        return True
    return False


def check_guess(word, key, guess_left, guess_progress):
    """Checks user guess"""
    if key in word:
        messagebox.showinfo("Correct guess", f"The word contains {key}")
        new_guess_progress = update_progress(word, guess_progress, key)
    else:
        messagebox.showinfo("Wrong guess", f"The word doesn't contain the letter {key}")
        guess_left -= 1
        new_guess_progress = guess_progress

    return guess_left, new_guess_progress


def start_game(word):
    """Start and manage the game."""
    guess_left, guess_progress, guessed_letters = initialize_game(word)

    # Create the main window
    root = Tk()
    root.title("Hangman")

    # Create and place the widgets
    Label(
        root,
        text="Can you guess what word I'm thinking of?",
    ).pack(pady=10)

    label_progress = Label(root, text=f"{guess_progress}")
    label_progress.pack(pady=5)

    max_errors = Label(root, text=f"Max Errors: {guess_left}")
    max_errors.pack(pady=10)

    letter_attempts = Label(root, text="Guessed letters: ...")
    letter_attempts.pack(pady=10)

    while True:
        key = get_guess(guessed_letters)
        guessed_letters.append(key)

        guess_left, guess_progress = check_guess(word, key, guess_left, guess_progress)

        guessed_letters_list = ", ".join(guessed_letters)

        label_progress.config(text=f"{guess_progress}")
        letter_attempts.config(text=f"Guessed letters: {guessed_letters_list}")
        max_errors.config(text=f"Max Errors: {guess_left}")

        if check_game_over(word, guess_progress, guess_left):
            break

    # Start the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    selected_word = select_word()
    start_game(selected_word)
