import turtle

#window height -> 540
#window width -> 640

def line(a, b, x, y):
    "Draw line from `(a, b)` to `(x, y)`."
    import turtle
    turtle.hideturtle()
    turtle.up()
    turtle.goto(a, b)
    turtle.down()
    turtle.goto(x, y)

def head(x, y, d):
    import turtle
    turtle.hideturtle()
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.circle(d)   

line(0, -540, 0 , 540)
line(-640, 0, 640, 0)

def draw_hanging_man():
    window = turtle.Screen()
    window.bgcolor("white")

    # Draw the gallows
    line(-200, -200, -200, 200)
    line(-200, 200, 0, 200)
    line(0, 200, 0, 150)

    # Draw the head
    head(0, 70, 40)
    
    # Draw the body
    line(0, 70, 0, -70)

    # Draw the left arm
    line(0, 0, -50, 50)

    # Draw the right arm
    line(0, 0, 50, 50)

    # Draw the left leg
    line(0, -70, -50, -120)

    # Draw the right leg
    line(0, -70, 50, -120)

    window.mainloop()

# Call the function to draw the hanging man
draw_hanging_man()
