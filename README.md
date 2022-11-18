#TODO
- Crear cuerpo de la culebra 

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)  

    def add_segment(self, position):
        new_segment = Turtle("circle")
        new_segment.color("#393E46")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    [![image.png](https://i.postimg.cc/13yDK9y4/image.png)](https://postimg.cc/8jnFpgJV)

- Garantizar como se mueva la snake

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):

            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            self.head.forward(MOVE_DISTANCE)

    [![image.png](https://i.postimg.cc/D0ZwzMhv/image.png)](https://postimg.cc/dkbYHnDp)

- Controlar el movimiento de la snake 

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
        
    [![image.png](https://i.postimg.cc/j2mnYbf0/image.png)](https://postimg.cc/CnCxb9Jm)

- Detectar colision con la comida

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    [![image.png](https://i.postimg.cc/dVKgmNH4/image.png)](https://postimg.cc/0bct9nqw)

- El manejo del puntaje 

    class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("#0D4C92")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    [![image.png](https://i.postimg.cc/dVKgmNH4/image.png)](https://postimg.cc/0bct9nqw)

- Detectar colision con los muros 

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor()> 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    [![image.png](https://i.postimg.cc/tT1rHFvs/image.png)](https://postimg.cc/Fd4byk4v)

- Detectar colision consigo misma 

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

    [![image.png](https://i.postimg.cc/dVKgmNH4/image.png)](https://postimg.cc/0bct9nqw)


