"""Simple guess the number game"""

import random


def generate_random_list():
    """generates a random list of 10 numbers"""
    start = random.randint(1, 91)
    random_number_list = list(range(start, start + 10))
    return random_number_list


def get_random_number(list_of_numbers):
    """selects a random number for given list"""
    random_number = random.choice(list_of_numbers)
    return random_number


def start_game():
    """Start guessing game"""
    list_of_numbers = generate_random_list()
    random_number = get_random_number(list_of_numbers)

    print(
        f"I'm thinking of a number between {list_of_numbers[0]} and {list_of_numbers[-1]}."
    )

    attempts = 3

    while attempts > 0:

        print("What number am I thinking?")
        guess = int(
            input(
                f"You have {attempts} {'attempt' if attempts == 1 else 'attempts'} left: "
            )
        )
        if guess == random_number:
            print("You guessed right!")
            break
        else:
            attempts -= 1
            if attempts > 0:
                if guess > random_number:
                    print("Guess lower.")
                else:
                    print("Guess higher")
            else:
                print(f"Better luck next time! I was thinking about {random_number}!")


if __name__ == "__main__":
    start_game()
    input("Press Enter to exit...")
