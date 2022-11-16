from turtle import Screen, Turtle

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#FF5733")
screen.title("Snake Game Jp")

starting_position = []

segment_1 = Turtle("square")
segment_1.color("white")

segment_2 = Turtle("square")
segment_2.color("white")
segment_2.goto(-20,0)

segment_2 = Turtle("square")
segment_2.color("white")
segment_2.goto(-40,0)


screen.exitonclick()