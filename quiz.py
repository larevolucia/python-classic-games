"""Simple quiz game"""

import random

quiz = {
    1: {"question": "What is the largest mammal in the world?", "answer": "Blue whale"},
    2: {
        "question": "Who wrote the play The Tempest?",
        "answer": ["William Shakespeare", "Shakespeare"],
    },
    3: {"question": "What is the chemical symbol for gold?", "answer": "Au"},
    4: {"question": "In what year did the Titanic sink?", "answer": 1912},
    5: {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
    6: {
        "question": "Who painted the Mona Lisa?",
        "answer": ["Leonardo da Vinci", "da Vinci"],
    },
    7: {
        "question": "What is the hardest natural substance on Earth?",
        "answer": "Diamond",
    },
    8: {
        "question": "Who was the first President of the United States?",
        "answer": "George Washington",
    },
    9: {"question": "Which element has the atomic number 1?", "answer": "Hydrogen"},
    10: {
        "question": "What is the longest river in the world?",
        "answer": ["The Nile River", "The Nile", "Nile", "Nile River"],
    },
}


def initialize_game_variables():
    """initialize variables"""
    score = 0
    # Get the keys and shuffle them
    keys = list(quiz.keys())
    random.shuffle(keys)

    return score, keys


def start_game():
    """starts the game"""
    # loop through shuffled keys
    score, keys = initialize_game_variables()

    for key in keys:
        print(quiz[key]["question"])
        answer = input().lower().strip()
        correct_answer = check_answer(answer, key)
        if correct_answer:
            score += 1
            print("Correct")
        else:
            print("Wrong")
    get_final_score(score)


def check_answer(answer, key):
    """check if answer is correct and add score"""
    correct_answers = quiz[key]["answer"]
    if isinstance(correct_answers, list):
        if any(answer == ans.lower().strip() for ans in correct_answers):
            return True
        else:
            return False
    else:
        if str(answer).lower().strip() == str(quiz[key]["answer"]).lower().strip():
            return True
        else:
            return False


def get_final_score(final_score):
    """get final score"""
    if final_score >= 8:
        print(f"Wow! You scored {final_score} points! That's great!")
    elif 5 < final_score < 8:
        print(f"Not too bad! You scored {final_score} points!")
    elif final_score == 5:
        print(f"You scored {final_score} points. Right in the middle.")
    else:
        print(f"You scored {final_score} points. Better luck next time.")


if __name__ == "__main__":
    start_game()
    input("Press any key to exit...")
