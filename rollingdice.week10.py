#how many sides there are on a dice. how mant dice there are and how many times the dice are rolled.

from random import randrange

class Dice:
    def __init__(self, sides):
        self.sides = sides #sides is used outside the class so self. 

    def roll(self):
        return randrange(1, self.sides + 1) #the random numbers that are generated are between 1-6 

class Dices:
    def __init__(self, dice_number, sides):
        self.dices = [] #empty list 
        for n in range(dice_number):
            self.dices.append(Dice(sides)) # the code will roll the number of dice with 6 sides  
 
    def roll(self, roll_number):
        result = [] #empty list, will contain the results of both for loops 
        for r in range(roll_number): #for how many rolls each dice has 
            roll_result = [] # will contain one result for each dice 
            for dice in self.dices:  #for the number of dice there are 
                roll_result.append(dice.roll())  # Roll the dice and add the result
            result.append(roll_result)  # Add the roll roll_results to results   
        return result 

def main():
    dice_number = int(input("How many dice would you like to roll? "))
    roll_number = int(input("How many rolls would you like to roll per dice? "))
    sides = 6
    dices = Dices(dice_number, sides) #instance
    rolls = dices.roll(roll_number)#instance
    for roll in rolls: #will output the code into how many lines depending on the number of rolls. e.g 4 rolls = 4 lists 
        print(roll)


main()


