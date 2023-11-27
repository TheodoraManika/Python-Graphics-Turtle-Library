# >=
# <=
# !=
# <
# >
# ==

# a < c,  b < c 
# a < b,  c < b
# b < a,  c < a 

a = int(input("Give number: "))
b = int(input("Give number: "))
c = int(input("Give number: "))

if c > b and c > a:
    print(c, "is the greatest")
elif b > a and b > c:
    print(b, "is the greatest")
else: 
    print(a, "is the greatest")