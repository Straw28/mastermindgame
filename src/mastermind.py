class MasterMind:
  def code_match(self, user_guess, actual_color_code): 
    def get_result_of_guess(self, user_guess_sequence, actual_color_sequence):
        correct_guesses = [-1] * len(actual_color_sequence) #initially we'll set everything to 0 (silver) and assume incorrect till we compare
        for i, guess in enumerate(actual_color_sequence):
            if int(user_guess_sequence[i]) == actual_color_sequence[i]:
                correct_guesses[i] = 1 #black = 1
            elif int(user_guess_sequence[i]) in actual_color_sequence:
                correct_guesses[i] = 0
        return correct_guesses
    
    return False




