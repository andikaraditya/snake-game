from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.color("red")
        self.speed("fastest")
        self.refresh()
        pass

    def refresh(self):
        self.goto(random.randrange(-260,60,20), random.randrange(-260,260,20))