import unittest
from src.mastermind import MasterMind

class MasterMindTests(unittest.TestCase):
  def test_canary(self):
    self.assertTrue(True)

  def test_code_match_results_in_matching_code(self):
    user_guess = [1,2,3,4,5,6]
    actual_code = [1,2,3,4,5,6]
    self.assertEqual(True, MasterMind().code_match(user_guess, actual_code))

if __name__ == '__main__': 
  unittest.main()

