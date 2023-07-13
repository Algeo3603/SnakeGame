import turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT, UP, LEFT, DOWN = 0, 90, 180, 270

class Snake:
    def __init__(self):
        self.snake = []
        self.createsnake()
        self.head = self.snake[0]

    def createsnake(self):
        for i in range((len(STARTING_POSITIONS))):
            s = turtle.Turtle()
            s.penup()
            s.shape("square")
            s.color("green")
            s.setposition(STARTING_POSITIONS[i])
            self.snake.append(s)

    def grow(self):
        g = self.snake[len(self.snake) - 1].clone()
        self.snake.append(g)

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].setposition(self.snake[i - 1].position())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)