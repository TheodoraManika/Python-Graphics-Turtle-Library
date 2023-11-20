import random
secret = random.randrange(1, 101) 
guess = 0
tries = 0 

while guess != secret:
    guess = int(input("Μαντεψε έναν αριθμό από το 1 ως 100: "))
    tries += 1
    if guess > secret:
        print("Πολύ μεγάλος!")
    elif guess < secret:
        print("Πολύ μικρός!")
    else:
        print("To βρήκες!")

print("You tried " + str(tries) + " times")