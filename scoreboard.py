from turtle import Turtle

"""when value is string type, much better to store it in variable"""
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.sety(270)
        self.update_score()

    def update_score(self):
        """display the score."""
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

    def game_over(self):
        """display game over text in home position (0,0)."""
        self.home()
        self.write("GAME OVER", False, ALIGNMENT, FONT)

    def increase_score(self):
        """increment score by 1."""
        self.clear()
        self.score += 1
        self.update_score()
