from turtle import Turtle

"""when value is string type, much better to store it in variable"""
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

FILE = open("data.txt")  # open data.txt.
CONTENT = FILE.read()  # read/return the content of data.txt.


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(CONTENT)
        self.hideturtle()
        self.color("white")
        self.penup()
        self.sety(270)
        self.update_score()

    def update_score(self):
        """display the score."""
        self.write(f"Score: {self.score} - Highest Score: {self.high_score}", False, ALIGNMENT, FONT)

    def reset_score(self):
        """reset score. if score is greater than high score, write it on data.txt."""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:    # write the highest score into data.txt.
                file.write(str(self.high_score))    # convert txt into str type.

        self.clear()
        self.score = 0
        self.update_score()

    def increase_score(self):
        """increment score by 1."""
        self.clear()
        self.score += 1
        self.update_score()
