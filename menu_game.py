import turtle 
import time

title = "Minecraft"
play_button = "Play"
settings_button = "Settings"
quit_button = "Quit"

score = 0
high_score = 0
difficulty = 0 # 0 = easy, 1 = medium, 2 = hard


sky = turtle.Turtle()
sky.hideturtle()
sky.screen.bgcolor('green')
sky.screen.setup(width=600, height=600)
sky.color('blue', 'blue')	
sky.penup()
sky.begin_fill()
sky.goto(-600, 0)
sky.pendown()
for i in range(2):
    sky.forward(1200)
    sky.left(90)
    sky.forward(600)
    sky.left(90)
sky.end_fill()

t = turtle.Turtle()
t.speed(0)
t.color("black")
t.penup()
t.hideturtle()
t.goto(0, 50)
t.write(title, align="center", font=("candara", 50, "bold"))

p = turtle.Turtle()
p.speed(0)
p.color("black")
p.penup()
p.hideturtle()
p.goto(0,0)
p.write(play_button, align="center", font=("candara", 30, "bold"))

q = turtle.Turtle()
q.speed(0)
q.color("black")
q.penup()
q.hideturtle()
q.goto(-200, -200)
q.write(quit_button, align="center", font=("candara", 18, "bold"))

s = turtle.Turtle()
s.speed(0)
s.color("black")
s.penup()
s.hideturtle()
s.goto(200, -200)
s.write(settings_button, align="center", font=("candara", 18, "bold"))

time.sleep(5)