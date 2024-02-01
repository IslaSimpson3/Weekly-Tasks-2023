#computer outputs if a number is even or odd

number = str(input("enter a number: "))

if number == int:
    if (number % 2) == 0:
        print("even")
    else:
        print("odd")
else:
    print("that is neither even or odd")
