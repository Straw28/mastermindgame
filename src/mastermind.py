class MasterMind:
  def code_match(self, user_guess, actual_color_code):

      correct_guesses = [''] * len(actual_color_code) 
      
      for i, guess in enumerate(actual_color_code):
          if user_guess[i] == actual_color_code[i]:
              correct_guesses[i] = 'black'
          elif user_guess[i] in actual_color_code:
              correct_guesses[i] = 'silver'
      
      return correct_guesses




