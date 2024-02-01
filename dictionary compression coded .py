#Given a string of text, print the number of times each letter in the alphabets a-z appear. Hint: “a” != “A”. eg. Given "the quick brown fox jumps over the lazy dog", the expected output is "a: 1, b: 1, c: 1, d: 1, e: 3 ......"

user_input = input("Enter a sentence: ").lower() #lower() is a built in functions = all the letters in the sentence become lowercase

def count_letters(sentence):
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    letter_counts = {letter: 0 for letter in lowercase} #goes threw all the letters in the lowercase string to see if the letters in my sence match

    for char in sentence:
        if char in lowercase:  # Checks if the character is in the lowercase alphabet
            letter_counts[char] += 1

    for letter in lowercase:
        if letter_counts[letter] > 0:  #only ouputs the letters amounts that are in the sentence. no 0
            print(f"{letter}: {letter_counts[letter]}", end=', ')
    print()


count_letters(user_input) #repeats the count_letter function with the usersinput. 




