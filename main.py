from turtle import Screen

#Cada una de las librerias o documentos lo que hace es llamar a cada una de ellas haciendo que cada una de ellas tengan su propia tarea sin necesidad de tener un solo codigo

from snake import Snake             #Importa la libreria de la cual viene la creacion de la snake
from food import Food               #Importa los valores de la comida de la snake
from scoreboard import Scoreboard   #Importa los la barra de puntos 
import time                         #La libreria funciona para todo aquel valor que tenga que ver con un lapso de tiempo 

screen = Screen()                   #Crea la ventana del juego
screen.setup(width=600, height=600) #Crea las dimensiones de la ventana
screen.bgcolor("#A0E4CB")           #El color de fondo 
screen.title("SNAKE GAME JP")       #El titulo del juego
screen.tracer(0)                    #Recoce las animaciones de la libreria de turtle

snake = Snake()                     #Utiliza los valores del index de snake 
food = Food()                       #Utiliza los valores del index de la comida
scoreboard = Scoreboard()           #Utiliza los valores del index de la barra de puntaje

#Con cada script se señaliza con las flechas su direccion de la snake
screen.listen()                     
screen.onkey(snake.up, "Up")        #con este direcciona la posicion hacia arriba
screen.onkey(snake.down, "Down")    #Con este direcciona la posicion hacia abajo
screen.onkey(snake.left, "Left")    #Con este direcciona la posicion hacia la izquierda
screen.onkey(snake.right, "Right")  #con este direcciona la posicion hacia la derecha

#con este script se señaliza los movimientos y animaciones de la snake 
game_is_on = True
while game_is_on:
    screen.update()                 #Con este se carga la pantalla de cada que la snake se mueve
    time.sleep(0.1)                 #Con este es la velocidad de a la que va la snake
    snake.move()                    #Con este hace que la serpiente se mueva por la pantalla

    if snake.head.distance(food) < 15:  #Cada vez que la snake coma la comida aparezca a cada distancia
        food.refresh()                  #Hace que aparezca la comida alrededor de la pantalla 
        snake.extend()                  #Cada que coma la snake crezca 
        scoreboard.increase_score()     #Cada que coma el puntaje vaya aumentando

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor()> 280 or snake.head.ycor() < -280:   #Por cada que se colisione con sigo misma se se acaba el juego
        game_is_on = False
        scoreboard.game_over()          #Muestra en la pantalla cada que se colisione con sigo misma muestra GAME OVER

    #Este ultimo segmento hace que la cabeza de la snake cada vez que este cerca del cuerpo se muestre como colision y termine el juego
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()                #Para que la ventana no se cierre de inmediato sin darle un click