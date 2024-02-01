threeNumbers = input("Enter 3 numbers separated by spaces: ")

# Split the input string into a list of three strings
numbers = threeNumbers.split()

# Convert the strings to integers
num1 = int(numbers[0])
num2 = int(numbers[1])
num3 = int(numbers[2])

equation1 = num1 + num2
finalEquation = num3 * equation1

print(finalEquation)
