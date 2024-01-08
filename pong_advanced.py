import turtle

class Obj:
    def __init__(x, y, color, shape, wid, len):
        self = turtle.Turtle()
        self.speed(0)
        self.color(color)
        self.shape(shape)
        self.shapesize(wid, len)
        self.penup()
        self.goto(x, y)

    def up(self):
        y = self.ycor()
        self.sety(y + 20)

    def down(self):
        y = self.ycor()
        self.sety(y - 20)

# settings for my window
win = turtle.Screen()
win.title("Welocome to my pong game!!!")
win.bgcolor("black")
win.setup(width = 800, height = 600)
win.tracer(0)

# Ρακέτα 1
p1 = Obj(-350, 0, "red", "square", 8, 2)

# Ρακέτα 2
p2 = Obj(350, 0, "yellow", "square", 8, 2)

# Μπάλα
ball= Obj(0, 0, "blue", "circle", 8, 2)

# Game loop
while True:
    win.update()