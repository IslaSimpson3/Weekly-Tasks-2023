#pig latin. vowel at the start = way at the end, (e.g eat = eatway) . otherwise = first letter + ay at the end, (e.g pig = igpay)


def piglatin(word):
    vowels = 'aeiou'
    word = word.lower()
    
   
    if word[0] in vowels: #checks the first letter in the word if its a vowel
        print(word + "way")
    else:
        word = word[1:] + word[0] + "ay"
        print(word) #outputing every letter in the word starting at the second letter, then adding the first letter then adding "ay"


userinput = input("Enter a word: ")
print(piglatin(userinput)) # perameter userinput is how changed to word
