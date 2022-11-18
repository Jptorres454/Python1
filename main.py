from turtle import Screen

#Cada una de las librerias o documentos lo que hace es llamar a cada una de ellas haciendo que cada una de ellas tengan su propia tarea sin necesidad de tener un solo codigo

from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#A0E4CB")
screen.title("SNAKE GAME JP")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

#Con cada screen se señaliza con las flechas su direccion de la snake
screen.listen()
screen.onkey(snake.up, "Up")        
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor()> 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()