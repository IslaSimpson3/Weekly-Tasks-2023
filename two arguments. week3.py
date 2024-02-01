#two arguments
fullName = input("Enter your name and your surname (surname is optional), in lowercase: ")
name = fullName.split()

firstName = name[0] #firstname

#if the length of the surname is larger than 0 then position 1 = surname 
if len(name) > 1: 
    surname = name[1]  # Surname is optional
    print("Hello there, " + firstName + " of " + surname + "!")
else:
    print("Hello, " + firstName + "!")

#in my 3 numbers task i used a split function for integers, i used chatGPT to help me use the same split function but for strings 
