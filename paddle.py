from turtle import Turtle

paddle_position = ((-350, ), (350, 0))


class Paddle(Turtle):
    def __init__(self, paddle_position):
        super().__init__()
        self.penup()
        self.goto(paddle_position)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_win=5, stretch_len=1)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor, new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor, new_y)

