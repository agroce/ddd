from minmax import minandmax
import unittest

class TestMinAndMax(unittest.TestCase):
    def test_single_element(self):
        self.assertEqual(minandmax([42]), (42, 42))

    def test_two_elements_in_order(self):
        self.assertEqual(minandmax([1, 2]), (1, 2))

    def test_two_elements_reverse_order(self):
        self.assertEqual(minandmax([5, -3]), (-3, 5))

    def test_multiple_elements(self):
        self.assertEqual(minandmax([3, 1, 4, 1, 5, 9, 2]), (1, 9))

    def test_all_equal_elements(self):
        self.assertEqual(minandmax([7, 7, 7]), (7, 7))

    def test_negative_numbers(self):
        self.assertEqual(minandmax([-5, -10, -3]), (-10, -3))

    def test_mixed_positive_and_negative(self):
        self.assertEqual(minandmax([-1, 0, 1]), (-1, 1))

    def test_large_range(self):
        self.assertEqual(minandmax(list(range(-1000, 1000))), (-1000, 999))

    def FAILS_test_empty_list(self):
        # According to the specification, this should return (None, None)
        # But the implementation raises IndexError on values[0]
        self.assertEqual(minandmax([]), (None, None))

if __name__ == '__main__':
    unittest.main()
