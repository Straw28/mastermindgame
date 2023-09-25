import unittest
from src.mastermind import MasterMind


class MasterMindTests(unittest.TestCase):
  def test_canary(self):
    self.assertTrue(True)

  def test_code_match_mixed_results(self):
    user_guess = ['yellow', 'red', 'cyan', 'violet', 'pink', 'orange']
    actual_code = ['yellow', 'red', 'green', 'orange', 'cyan', 'pink']

    response = MasterMind().code_match(user_guess, actual_code)
    expected = ['black', 'black', 'silver', '', 'silver', 'silver']

    self.assertEqual(expected, response)



if __name__ == '__main__': 
  unittest.main()

