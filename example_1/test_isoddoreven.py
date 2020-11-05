import isoddoreven as oe
import unittest


class TestIsOddOrEven(unittest.TestCase):
    def test_odd_even(self):
        self.assertEqual(oe.is_odd_or_even(1), 'Odd')
        self.assertEqual(oe.is_odd_or_even(2), 'Even')

        with self.assertRaises(TypeError):
            oe.is_odd_or_even('abc')
            oe.is_odd_or_even(True)


if __name__ == "__main__":
    unittest.main()
