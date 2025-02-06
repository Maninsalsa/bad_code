import unittest

class TestTwoSum(unittest.TestCase):
    def test_simple_case(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_non_adjacent_numbers(self):
        self.assertEqual(two_sum([1, 4, 6, 8], 10), [1, 3])

    def test_negative_numbers(self):
        self.assertEqual(two_sum([-3, 4, 3, 90], 0), [0, 2])

    def test_no_solution(self):
        self.assertIsNone(two_sum([1, 2, 3], 10))

    def test_large_list(self):
        nums = list(range(1, 10001))
        self.assertEqual(two_sum(nums, 19999), [9997, 9998])

if __name__ == "__main__":
    unittest.main()