a = int(input("Give number: "))
b = int(input("Give number: "))
c = int(input("Give number: "))

max = a
if b > max:
    max = b
elif c > max:
    max = c

print(max, "is the  greatest")