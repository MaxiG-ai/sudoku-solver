import unittest
import numpy as np

from main import check_numbers

class TestCheckNumbersFunction(unittest.TestCase):

    def test_valid_input(self):
        # Test with a valid input array
        numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertTrue(check_numbers(numbers))

    def test_invalid_length(self):
        # Test with an array of invalid length
        numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8])
        self.assertFalse(check_numbers(numbers))

    def test_duplicate_numbers(self):
        # Test with an array containing duplicate numbers
        numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 8])
        self.assertFalse(check_numbers(numbers))

    def test_out_of_range_numbers(self):
        # Test with an array containing numbers out of range
        numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 10])
        self.assertFalse(check_numbers(numbers))

    def test_empty_array(self):
        # Test with an empty array
        numbers = np.array([])
        self.assertFalse(check_numbers(numbers))

    def test_non_integer_numbers(self):
        # Test with an array containing non-integer numbers
        numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9.0])
        self.assertTrue(check_numbers(numbers))  # Note: This might be expected to return False depending on your requirements

    def test_input_not_numpy_array(self):
        # Test with input not being a numpy array
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        with self.assertRaises(TypeError):
            check_numbers(numbers)

if __name__ == '__main__':
    unittest.main()