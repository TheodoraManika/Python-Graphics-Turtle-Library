import random
numbers = []

for i in range(51):
    num = random.randrange(0, 501)
    numbers.append(num)

print(numbers)