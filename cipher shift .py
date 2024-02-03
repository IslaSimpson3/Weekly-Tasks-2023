#Cipher shift
#implement a Caesar Cipher function that takes a string and shift amount, outputs the encrypted string.
#Input: hello word
#Shift by: 7
#Output: olssv dvysk

shift = {
   "a": "h", "b": "i", "c": "j", "d": "k", "e": "l", "f": "m", 
   "g": "n", "h": "o", "i": "p", "j": "q", "k": "r", "l": "s", 
   "m": "t", "n": "u", "o": "v", "p": "w", "q": "x", "r": "y", 
   "s": "z", "t": "a", "u": "b", "v": "c", "w": "d", "x": "e", 
   "y": "f", "z": "g"
}

reverse_shift = {v: k for k, v in shift.items()}
text = input("Enter a word: ").lower()
output = " "

for c in text:   #will loop around the same amount as the number of letters in the text 
    if c in shift:  #if the character/letter is in the list above then the character(key) will assign its
        word = shift[c]
    else:
        word = c #if there is a space, leave the space 
    output += word 

print(output)
