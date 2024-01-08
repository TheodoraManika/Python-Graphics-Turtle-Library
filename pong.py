import turtle

# settings for my window
win = turtle.Screen()
win.title("Welocome to my pong game!!!")
win.bgcolor("black")
win.setup(width = 800, height = 600)
win.tracer(0)

# Ρακέτα 1
p1 = turtle.Turtle()
p1.speed(0)
p1.color("red")
p1.shape("square")
p1.shapesize(stretch_wid = 8, stretch_len = 6)
p1.penup()
p1.goto(-350, 0)


# Ρακέτα 2

# Μπάλα

# Game loop
while True:
    win.update()