from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

#EL codigo muestra que cada que la snake coma de un punto en el scoreboard

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("#0D4C92")       #Se cambia el color de la comida para que sea mas visible
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self): 
        self.score += 1
        self.clear()
        self.update_scoreboard()