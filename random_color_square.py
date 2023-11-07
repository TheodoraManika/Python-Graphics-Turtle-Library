# ΝΑ ΦΤΙΑΞΕΤΕ 5 ΤΕΤΡΑΓΩΝA  ΣΕ ΤΥΧΑΙΕΣ ΘΕΣΕΙΣ ΜΕ ΔΙΑΦΟΡΕΤΙΚΟ ΧΡΩΜΑ ΧΕΛΩΝΑΣ ΚΑΘΕ ΦΟΡΑ 
import turtle
import random

# Create obj and initialize shape
fred = turtle.Pen()
fred.shape("turtle")

#helpful list with every color
colors = ["red", "green", "blue", "orange", "yellow"]

#function that makes a square
def square(cor, col, size = 50):
    fred.up()
    fred.goto(cor[0],cor[1])
    fred.down()
    fred.color(col)
    for i in range(4):
        fred.forward(size)
        fred.left(90)
    

#loop that makes a square 5 times and is given random values    
for i in range(5):
    x = random.randrange(-200, 201)
    y = random.randrange(-200, 201)
    col = random.choice(colors)
    size = random.randrange(50, 200)
    square([x, y ], col, size)
    fred.screen.clear()

fred.screen.exitonclick()   