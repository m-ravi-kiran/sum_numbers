import unittest

from app import Sum


class SimpleTest(unittest.TestCase):
    """Tests all the functions of Sum class"""

    def test_is_num(self):
        """Tests if is_num function is working properly."""
        self.assertTrue(Sum().is_num(1), True)
        self.assertTrue(Sum().is_num('1'), True)
        self.assertFalse(Sum().is_num('1.0'), False)
        self.assertFalse(Sum().is_num('a'), False)

    def test_validate(self):
        """Tests if validate function is working properly."""
        self.assertTrue(Sum(3).validate(1, 2, 3))
        self.assertFalse(Sum(3).validate(1, 2))
        self.assertFalse(Sum(3).validate((1, 2, 'a')))

    def test_teen(self):
        """Tests if get_teen function is working properly."""
        self.assertEqual(Sum().get_teen(1), 1)
        self.assertEqual(Sum().get_teen(13), 0)
        self.assertEqual(Sum().get_teen(19), 0)
        self.assertEqual(Sum().get_teen(15), 15)

    def test_sum(self):
        """Tests if sum_numbers function is working properly."""
        self.assertEqual(Sum(3).sum_numbers(1, 2, 3), 6)
        self.assertEqual(Sum(3).sum_numbers(1, 2, 14), 3)
        self.assertEqual(Sum(3).sum_numbers(1, 2, 15), 18)


if __name__ == '__main__':
    unittest.main()
