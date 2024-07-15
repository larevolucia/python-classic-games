"""General trivia using tkinter"""

import random
from tkinter import Tk, Entry, Button, Label, messagebox


class QuizApp:
    """Quiz App stores quiz questions and global variables"""

    def __init__(self, root):
        self.quiz = {
            1: {
                "question": "What is the largest mammal in the world?",
                "answer": "Blue whale",
            },
            2: {
                "question": "Who wrote the play The Tempest?",
                "answer": ["William Shakespeare", "Shakespeare"],
            },
            3: {"question": "What is the chemical symbol for gold?", "answer": "Au"},
            4: {"question": "In what year did the Titanic sink?", "answer": 1912},
            5: {
                "question": "Which planet is known as the Red Planet?",
                "answer": "Mars",
            },
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
            9: {
                "question": "Which element has the atomic number 1?",
                "answer": "Hydrogen",
            },
            10: {
                "question": "What is the longest river in the world?",
                "answer": ["The Nile River", "The Nile", "Nile", "Nile River"],
            },
        }
        self.score = 0
        self.current_question_index = 0
        self.questions_keys = []
        self.root = root
        self.entry_answer = None
        self.label_question = None
        self.label_score = None
        self.button_check = None

        self.shuffle_quiz_questions()
        self.setup_ui()
        self.display_question()

    def shuffle_quiz_questions(self):
        """Initializes game variables"""
        keys = list(self.quiz.keys())
        random.shuffle(keys)
        self.questions_keys = keys

    def check_answer(self):
        """Compare user answers with stored correct answers"""

        user_answer = self.entry_answer.get().strip()
        correct_answer = self.quiz[self.questions_keys[self.current_question_index]][
            "answer"
        ]

        if isinstance(correct_answer, list):
            if user_answer in map(str.lower, correct_answer):
                self.score += 1
                messagebox.showinfo("Correct!", "Well done!")
            else:
                messagebox.showerror(
                    "Incorrect", f"The correct answer is: {correct_answer[0]}"
                )
        else:
            if user_answer.lower() == str(correct_answer).lower():
                self.score += 1
                messagebox.showinfo("Correct!", "Well done!")
            else:
                messagebox.showerror(
                    "Incorrect", f"The correct answer is: {correct_answer}"
                )

        self.current_question_index += 1

        if self.current_question_index < len(self.questions_keys):
            self.display_question()
            self.label_score.config(text=f"Your score: {self.score}")
        else:
            self.label_question.config(text="Quiz over!")
            self.label_score.config(text=f"Your final score: {self.score}")
            self.entry_answer.pack_forget()
            self.button_check.pack_forget()

    def display_question(self):
        """Display questions"""
        question = self.quiz[self.questions_keys[self.current_question_index]][
            "question"
        ]
        self.label_question.config(text=question)
        self.entry_answer.delete(0, "end")

    def setup_ui(self):
        """Ste ups Tkinter UI"""
        self.root.title("Trivia")

        self.label_question = Label(self.root, text="")
        self.label_question.pack(pady=10)

        self.entry_answer = Entry(self.root)
        self.entry_answer.pack(pady=5)

        self.button_check = Button(
            self.root, text="Check answer", command=self.check_answer
        )
        self.button_check.pack(pady=5)

        self.label_score = Label(self.root, text=f"Your score: {self.score}")
        self.label_score.pack(pady=10)


def start_game():
    """Starts the game"""
    root = Tk()
    app = QuizApp(root)  # pylint: disable=unused-variable
    root.mainloop()


if __name__ == "__main__":
    start_game()
