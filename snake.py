from turtle import Turtle,Screen
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]

MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        snake_length = len(self.segments)
        self.tail = self.segments[snake_length-1]
        self.segment_cordinates = []

    def create_snake(self):
        for cordinates in STARTING_POSITION:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            # new_segment.speed(1)

            new_segment.penup()
            new_segment.goto(cordinates)
            self.segments.append(new_segment)

    def add_segment(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        last_cordinates = (self.tail.pos())
        new_segment.goto(last_cordinates)
        self.segments.append(new_segment)

    def update_cord(self):
        self.segment_cordinates.clear()
        for seg in self.segments:
            self.segment_cordinates.append(seg.pos())


    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x_pos = self.segments[i - 1].xcor()
            new_y_pos = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x_pos, new_y_pos)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)


    def right(self):

        if self.head.heading()!=180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)

    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)