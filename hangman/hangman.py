"""Hangman game"""

#!/usr/bin/env python3

import random


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
        key = input("Guess a letter: ").lower()
        if key.isalpha() and len(key) == 1:
            if key not in guessed_letters:
                return key
            else:
                print("You tried that letter already!")
        else:
            print("Please enter a single alphabetic character.")


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
        print("You win! The word was: " + word)
        return True
    if guess_left == 0:
        print("You lose! The word was " + word)
        return True
    return False


def start_game(word):
    """Start and manage the game."""
    guess_left, guess_progress, guessed_letters = initialize_game(word)
    print(f"You have {guess_left} guesses to figure out the word.")

    while True:
        print("Current progress: " + guess_progress)
        key = get_guess(guessed_letters)
        guessed_letters.append(key)

        if key in word:
            print("The word contains " + key)
            guess_progress = update_progress(word, guess_progress, key)
        else:
            print("The word doesn't contain the letter " + key)
            guess_left -= 1

        guessed_letters_list = ", ".join(guessed_letters)
        print(f"Guessed letters: {guessed_letters_list}")
        print(f"Guesses left: {guess_left}")

        if check_game_over(word, guess_progress, guess_left):
            break


if __name__ == "__main__":
    selected_word = select_word()
    start_game(selected_word)
    input("Press Enter to exit...")
