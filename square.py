import turtle
import random 

def square(size = 50):
    for i in range(4):
        fred.forward(size)
        fred.left(90)

fred = turtle.Pen()
fred.hideturtle()
fred.shape("turtle")

for i in range(4):
    x = random.randrange(-200, 201)
    y = random.randrange(-200, 201)

    fred.up()
    fred.goto(x,y)
    fred.down()
    square(100)

fred.screen.exitonclick()

# Μπορείτε να γράψετε πρόγραμμα που να 
# σχεδιάζει ένα τετράγωνο με πλευρά 100 pixels σε τυχαία θέση στην οθόνη; Τα όρια της οθόνης σου 
# (x, y) είναι από -200 μέχρι 200
