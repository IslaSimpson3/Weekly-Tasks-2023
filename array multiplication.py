#list multiplication

userInput = input("enter a list of numbers, separated by spaces")

numbers = userInput.split()

numlist = [int(num) for num in numbers] # the userinput is split into individual numbers. then within the list the numbers are added to the list using a loop

print(numlist)

answer = 1
for i in numlist:
    answer = answer * i

print(answer)


