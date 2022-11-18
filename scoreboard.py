from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

#EL codigo muestra que cada que la snake coma de un punto en el scoreboard

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0              #Muestra el puntaje predeterminado que es 0
        self.color("#0D4C92")       #Se cambia el color de la comida para que sea mas visible
        self.penup()                #Levanta el lapiz que muestra las direcciones que ha ido la serpiente
        self.goto(0, 270)           #Coordenadas en la cual va estar posicionada la serpiente 
        self.hideturtle()           #Este metodo se utiliza para no mostrar la libreria en pantalla 
        self.update_scoreboard()    #Este se utiliza para que cada vez que la tortuga coma se acutalize la barra de puntaje

    #Este segmento señaliza como se va actualizando la barra de puntaje cada que la serpiente coma
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    #Muestra en pantalla cada que haya colision o se choque con las paredes muestre en pantalla GAME OVER
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    #Cada que se inicia el GAME Se reinicie el puntaje y no muestre el puntaje anterior
    def increase_score(self): 
        self.score += 1
        self.clear()
        self.update_scoreboard()