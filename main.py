from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")
starting_position = [(0,0), (-20,0), (-40,0)]
segments = []
#Turtle.speed()

for position in starting_position:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    segments.append(segment)

game_is_on = True
while game_is_on:
    screen.update()
    for segment in segments:
        segment.forward(20)


screen.exitonclick()

