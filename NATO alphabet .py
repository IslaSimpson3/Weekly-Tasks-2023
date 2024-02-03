# NATO alphabet - dictionary
 

NATO = {
   "a": "alpha", "b": "bravo", "c": "charlie", "d": "delta", "e": "echo", "f": "foxtrot", 
   "g": "golf", "h": "hotel", "i": "india", "j": "juliett", "k": "kilo", "l": "lima", 
   "m": "mike", "n": "november", "o": "oscar", "p": "papa", "q": "quebec", "r": "romeo", 
   "s": "sierra", "t": "tango", "u": "uniform", "v": "victor", "w": "whiskey", "x": "xray", 
   "y": "yankee", "z": "zulu"
}

reverse_NATO = {v: k for k, v in NATO.items()} # v = value and k = key. this line of code will swap the two around. it will know if the values need to me swapped as the users input would either be in the table or not 


text = input("Enter a word: ").lower() #turns it into lowercase 


 
if text in reverse_NATO:
        print(reverse_NATO[text]) #if a word from the table is inputted the letter will be outputted. 
else:
    output = []  #making an empty list for the words 
    for i in text:
        if i in NATO:# Convert text to lowercase to match the keys in the table. 
            word = NATO.get(i) #make a for loop to go though the text, each letter in the text is in the table. the get function will get the word assigned with the letter in the text from the table. and output it. 
            output.append(word)
        else:
            word = i #removes spaces 

    print(output)






   
