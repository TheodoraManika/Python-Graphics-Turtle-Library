import random
secret = random.randrange(1, 101) 
=

guess = int(input("Μαντεψε έναν αριθμό από το 1 ως 100: "))

if guess > secret:
    print("Πολύ μεγάλος!")
elif guess < secret:
    print("Πολύ μικρός!")
else:
    print("To βρήκες!")