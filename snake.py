from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            if position[0] == 0:
                segment = Turtle("circle")
            else:
                segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def move(self):
        # snake direction would be decided by the head or first segment,
        # thus tracing by the remaining segments for easy follow movement
        for seq_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seq_num - 1].xcor()
            new_y = self.segments[seq_num - 1].ycor()
            self.segments[seq_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def grow(self):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        new_x = self.segments[len(self.segments)-1].xcor()
        new_y = self.segments[len(self.segments)-1].ycor()
        segment.goto(new_x, new_y)
        self.segments.append(segment)

    def new_game(self):
        for segment_b in self.segments:
            segment_b.goto(1000,1000)
        self.segments.clear()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
