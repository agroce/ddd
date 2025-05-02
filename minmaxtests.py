from minmax import minandmax
import unittest

class Box:
    """Wraps a value and tracks identity for equality testing."""
    def __init__(self, value, label):
        self.value = value
        self.label = label  # Unique identifier to distinguish objects with same value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value and self.label == other.label

    def __repr__(self):
        return f"Box({self.value}, '{self.label}')"

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

    def test_min_max_duplicates(self):
        self.assertEqual(minandmax([3, 1, 4, 1, 5, 9, 1, 9]), (1, 9))

    def test_empty_list(self):
        self.assertEqual(minandmax([]), (None, None))

    def test_custom_objects_first_occurrence(self):
        a = Box(5, 'a')  # Should be max
        b = Box(1, 'b')  # Should be min
        c = Box(5, 'c')  # Same value as max
        d = Box(1, 'd')  # Same value as min
        e = Box(3, 'e')

        result = minandmax([a, b, c, d, e])
        self.assertEqual(result, (b, a))  # First 1 and first 5

if __name__ == '__main__':
    unittest.main()
