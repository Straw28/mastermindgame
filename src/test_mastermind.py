import unittest
#from src.mastermind import code_match
from mastermind import code_match
from mastermind import Colors
from enum import Enum


class MasterMindTests(unittest.TestCase):
  def test_canary(self):
    self.assertTrue(True)

  def test_code_match_mixed_results(self):
    
    user_guess = [Colors.YELLOW, Colors.RED, Colors.CYAN, Colors.VIOLET, Colors.PINK, Colors.ORANGE]
    actual_code = [Colors.YELLOW, Colors.RED, Colors.GREEN, Colors.ORANGE, Colors.CYAN, Colors.PINK]

    response = code_match(user_guess, actual_code)
    
    expected = [Colors.BLACK, Colors.BLACK, Colors.SILVER, '', Colors.SILVER, Colors.SILVER]

    self.assertEqual(expected, response)



if __name__ == '__main__': 
  unittest.main()

