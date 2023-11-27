import random
numbers = []

for i in range(51):
    num = random.randrange(0, 501)
    numbers.append(num)

print(numbers)

max = numbers[0]
for i in range(1, len(numbers)):
    if max < numbers[i]:
        max = numbers[i]

print(max, "is the  greatest")