STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
from turtle import Turtle
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0



class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_seg = Turtle(shape="square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)
        self.segments.append(new_seg)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments - 1), 0, -1):
            newx = self.segments[seg_num - 1].xcor()
            newy = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(newx, newy)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading != LEFT:
            self.segments[0].setheading(RIGHT)