from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="none", fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Label
        self.score = Label(text="score:0", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        # Buttons
        true_image = PhotoImage(file="images/true.png")
        self.true = Button(image=true_image, highlightthickness=0, command=self.true_press)
        self.true.grid(column=0, row=2)

        false_image = PhotoImage(file="images/false.png")
        self.false = Button(image=false_image, highlightthickness=0, command=self.false_press)
        self.false.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def true_press(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_press(self):
        self.give_feedback(self.quiz.check_answer("False"))

    # THERE IS A PROBLEM IN THIS BLOCK OF CODE IT ONLY RUNS THE ELSE STATEMENT
    def give_feedback(self, is_right):
        # is_right = is_right == "True"

        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
