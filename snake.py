from turtle import Screen, Turtle
import time 


screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#34495E")
screen.title("Snake Game Jp")


starting_position = [(0,0), (-20,0), (-40,0)]


segments = []


for position in starting_position:
    new_segment = Turtle("turtle")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


game_is_one = True


while game_is_one:
    screen.update()
    time.sleep(0.1)
    for seg in segments:
        seg.forward(20)



screen.exitonclick()