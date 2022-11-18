from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]   #Posicion en la cual va empezar en la pantalla 
MOVE_DISTANCE = 10                                  #Cada cuanto se va a mover los recuadros de la serpiente 
UP = 90                                             #El angulo en el cual se van a mover o en que posicion va ir
DOWN = 270                                          #El angulo en el cual se van a mover o en que posicion va ir
LEFT = 180                                          #El angulo en el cual se van a mover o en que posicion va ir
RIGHT = 0                                           #El angulo en el cual se van a mover o en que posicion va ir

#La clase siguiente muestra todos los componentes que va tener la serpiente 
class Snake:

    def __init__(self):
        self.segments = []                          #Crea los segmentos de la serpiente 
        self.create_snake()                         #Crea la serpiente o unos parametros
        self.head = self.segments[0]                #Crea la cabeza de la serpiente con sus propios parametros

    #Crea la serpiente y en que posicion esta
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)  

    def add_segment(self, position):
        new_segment = Turtle("circle")              #La figura de de la cual va estar compuesta la serpiente
        new_segment.color("#393E46")                #Color de la serpiente 
        new_segment.penup()                         #Levanta el lapiz que muestra las direcciones que ha ido la serpiente
        new_segment.goto(position)                  #Coordenadas en la cual va estar posicionada la serpiente 
        self.segments.append(new_segment)           #Llama todos los segmentos en uno

    #Cuanto se va a extender la serpiente de cada que coma la serpiente
    def extend(self):
        self.add_segment(self.segments[-1].position())

    #La distancia de que va a recorrer la serpiente 
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):

            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            self.head.forward(MOVE_DISTANCE)

    #El direccionamiento de que va a tener la serpiente dependiendo las flechas del teclado
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