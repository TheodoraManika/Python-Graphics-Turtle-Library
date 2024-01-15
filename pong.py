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
p1.shapesize(stretch_wid = 8, stretch_len = 2)
p1.penup()
p1.goto(-350, 0)

def p1_up():
    y = p1.ycor()
    p1.sety(y + 20)

def p1_down():
    y = p1.ycor()
    p1.sety(y - 20)

# Ρακέτα 2
p2 = turtle.Turtle()
p2.speed(0)
p2.color("yellow")
p2.shape("square")
p2.shapesize(stretch_wid = 8, stretch_len = 2)
p2.penup()
p2.goto(350, 0)

def p2_up():
    y = p2.ycor()
    p2.sety(y + 20)

def p2_down():
    y = p2.ycor()
    p2.sety(y - 20)

# Μπάλα
ball= turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("blue")
ball.shapesize(stretch_wid = 2, stretch_len = 2)
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = -2

def move_ball():
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #Border checking
    if ball.ycor() > 290: 
        ball.sety(290)
        ball.dy *=-1
    if ball.ycor() < -290: 
        ball.sety(-290)
        ball.dy *=-1
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *=-1
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *=-1


#keyboard binding
win.listen()
win.onkeypress(p1_up, "w")
win.onkeypress(p1_down, "s")
win.onkeypress(p2_up, "Up")
win.onkeypress(p2_down, "Down")

# Game loop
while True:
    win.update()