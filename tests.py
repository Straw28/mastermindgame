import unittest
from src.main import Feedback

#Canary Test
class TestCanary(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

   

#No Black or Silver
class AllIncorrect(unittest.TestCase):
    def test_incorrect_guess(self):
        feedback = Feedback()

        actual_color_sequence = [1,2,3,4,5,6]
        user_guess_sequence = [6,5,4,3,2,1]
        result = feedback.get_result_of_guess(user_guess_sequence, actual_color_sequence)

        self.assertNotIn(1, result)
        self.assertNotIn(0, result)
    
class IncorrectBlack(unittest.TestCase):
    def test_incorrect_black_count(self):
        feedback = Feedback()

        user_guess_sequence = [1,2,3,4,5,6]
        actual_color_sequence = [1,2,3,4,7,8]

        result = feedback.get_result_of_guess(user_guess_sequence,actual_color_sequence)

        self.assertEqual(result.count(1),2)


class IncorrectSilver(unittest.TestCase):
    def test_incorrect_silver_count(self):
        feedback = Feedback()

        user_guess_sequence = [1,2,3,4,5,6]
        actual_color_sequence = [6,5,4,3,2,1]

        result = feedback.get_result_of_guess(user_guess_sequence,actual_color_sequence)

        self.assertEqual(result.count(0),3)
    
if  __name__ == '__main__':
    unittest.main()