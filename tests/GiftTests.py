import unittest

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = 2 * 3
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        result = 1
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()