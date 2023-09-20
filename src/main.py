import tkinter as tk
#import pytest as pt
#from PIL import Image
import random



class ColorCode():
    
    game_color_code = set() #set bc the colors have to be distinct 
    
    def return_code(self):
        while len(self.game_color_code) < 6:
            self.game_color_code.add(random.randint(1,10))
        return list(self.game_color_code)


class Color():
#we'll map the color to the number here, and maye do the display stuff with pillow, do we need another class for that. ie a class "display game"
    orange = 2 #keep the same colors to numbers
    silver = 0
    black = 1

class Feedback():

    def get_result_of_guess(self, user_guess_sequence, actual_color_sequence):
        correct_guesses = [-1] * len(actual_color_sequence) #initially we'll set everything to 0 (silver) and assume incorrect till we compare
        for i, guess in enumerate(actual_color_sequence):
            if int(user_guess_sequence[i]) == actual_color_sequence[i]:
                correct_guesses[i] = 1 #black = 1
            elif int(user_guess_sequence[i]) in actual_color_sequence:
                correct_guesses[i] = 0
        return correct_guesses
        


# class GameUI(): 

#     game_start =  True
#     number_of_guesses = 5 #5 for testing purposes
#     user_guess_sequence = []
#     color = ColorCode()
#     actual_color_sequence = color.return_code()
#     result = Feedback()

#     while True:
#         user_guess_string = input("Enter your guess: \n")
#         user_guess_sequence = user_guess_string.split(',')
#         print(result.get_result_of_guess(user_guess_sequence, actual_color_sequence))
#         number_of_guesses -= 1
        
#         if (number_of_guesses <= 0) or (-1 not in (result.get_result_of_guess(user_guess_sequence, actual_color_sequence))): # the second condition is checking to make sure there are no silver boxes
#             print("The correct sequence was actually: ", actual_color_sequence)
#             break


