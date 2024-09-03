from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("green")
        self.refresh()

    def refresh(self):
        """show food in a random location."""
        self.penup()
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))
