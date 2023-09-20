import tkinter as tk
import random



class ColorCode():
    
    game_color_code = set() 
    
    def return_code(self):
        while len(self.game_color_code) < 6:
            self.game_color_code.add(random.randint(1,10))
        return list(self.game_color_code)


class Feedback():

    def get_result_of_guess(self, user_guess_sequence, actual_color_sequence):
        correct_guesses = [-1] * len(actual_color_sequence) 
        for i, guess in enumerate(actual_color_sequence):
            if int(user_guess_sequence[i]) == actual_color_sequence[i]:
                correct_guesses[i] = 1 
            elif int(user_guess_sequence[i]) in actual_color_sequence:
                correct_guesses[i] = 0
        return correct_guesses
        



