import unittest
#from src.mastermind import code_match
from mastermind import code_match
from mastermind import Colors
from enum import Enum


class MasterMindTests(unittest.TestCase):
  def test_canary(self):
    self.assertTrue(True)

  def test_code_match_mixed_results(self):
    color = Colors(Enum)
    
    user_guess = [color.YELLOW, color.RED, color.CYAN, color.VIOLET, color.PINK, color.ORANGE]
    actual_code = [color.YELLOW, color.RED, color.GREEN, color.ORANGE, color.CYAN, color.PINK]

    response = code_match(user_guess, actual_code)
    
    expected = [color.BLACK, color.BLACK, color.SILVER, '', color.SILVER, color.SILVER]

    self.assertEqual(expected, response)



if __name__ == '__main__': 
  unittest.main()

