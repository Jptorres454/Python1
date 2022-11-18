from turtle import Turtle
import random


#Este codigo muestra la comida con la cual se va alimentar la serpinet para crecer 
class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("#3B185F")
        self.speed("fastest")
        self.refresh()

#Muestra que cada vez que la serpiente coma la comida vuelva en un lugar aleatorio
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
