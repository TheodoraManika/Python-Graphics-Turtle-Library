# State of the game if we contiue being in the app
calc_state = "y"

#loop for continuing being in the app
while calc_state == "y":
    #input the numbers and symbols
    number1 = int(input("Give first number: \n"))
    number2 = int(input("Give second number: \n"))
    symbol = input("Give symbol: \n")

    #do the right action based on the symbol we gave
    if symbol == "+":
        print(str(number1) + symbol + str(number2) + "= ", number1 + number2)
    elif symbol == "-":
        print(str(number1) + symbol + str(number2) + "= ", number1 - number2)
    elif symbol == "*":
        print(str(number1) + symbol + str(number2) + "= ", number1 * number2)
    elif symbol == "/":
        print(str(number1) + symbol + str(number2) + "= ", number1 / number2)
    elif symbol == "//":
        print(str(number1) + symbol + str(number2) + "= ", number1 // number2)
    elif symbol == "%":
        print(str(number1) + symbol + str(number2) + "= ", number1 % number2)
    elif symbol == "**":
        print(str(number1) + symbol + str(number2) + "= ", number1 ** number2)
    else:
        print("Wrong symbol. Try again")
        continue

    #Ask id they want to continue being in the calculator
    calc_state = input("Do you want to continue? Type y or n \n")
