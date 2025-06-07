import unittest
from unittest.mock import patch
import tools

class TestTools(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(tools.greet("Alice"), "Hello, Alice!")
        self.assertEqual(tools.greet("Bob"), "Hello, Bob!")

    def test_roll_dice(self):
        with patch('random.randint') as mock_randint:
            mock_randint.return_value = 3
            result = tools.roll_dice(5)
            self.assertEqual(result, [3, 3, 3, 3, 3])
            self.assertEqual(mock_randint.call_count, 5)

    def test_generate_lottery_numbers(self):
        with patch('random.sample') as mock_sample:
            mock_sample.return_value = [7, 14, 21, 28, 35, 42]
            result = tools.generate_lottery_numbers()
            self.assertEqual(result, [7, 14, 21, 28, 35, 42])
            mock_sample.assert_called_once_with(range(1, 50), 6)

if __name__ == '__main__':
    unittest.main()
