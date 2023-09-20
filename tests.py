import unittest
from src.main import Feedback

#Canary Test
class TestCanary(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

   

#No Black or Silver
class ComIncorrect(unittest.TestCase):
    def test_incorrect_guess(self):
        feedback = Feedback()

        game_color_code = [1,2,3,4,5,6]
        user_guess = [6,5,4,3,2,1]
        result = feedback.get_result_of_guess(user_guess, game_color_code)

        self.assertNotIn(1, result)
    

if  __name__ == '__main__':
    unittest.main()