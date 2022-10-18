from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]

class Snakes:

    def __init__(self) -> None:
        self.body = []
        self.create_snake()
        self.head = self.body[0]


    def create_snake(self):
        for i in STARTING_POSITION:
            self.add_segment(i)
        pass


    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.body.append(new_segment)


    def extend(self):
        self.add_segment(self.body[-1].position())
        

    def reset(self):
        for i in self.body:
            i.goto(1000,1000)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]


    def move(self):
        for i in range(len(self.body)-1, 0, -1):
            new_x = self.body[i-1].xcor()
            new_y = self.body[i-1].ycor()
            self.body[i].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)


    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)


    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)


    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

