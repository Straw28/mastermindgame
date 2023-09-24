import unittest
from src.mastermind import MasterMind

class MasterMindTests(unittest.TestCase):
  def test_canary(self):
    self.assertTrue(True)

  def test_code_match_results_in_matching_code(self):
    user_guess = ['orange','blue ','green','yellow','red','pink']
    actual_code = ['orange','blue ','green','yellow','red','pink']

    response = MasterMind().code_match(user_guess, actual_code)
    expected = ['black'] * 6
    
    self.assertEqual(expected, response)

if __name__ == '__main__': 
  unittest.main()

