from math import pi
import unittest
import calculator as cl


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(cl.add(1, 2), 3)
        self.assertEqual(cl.add(-1, 2), 1)
        self.assertEqual(cl.add(1, -2), -1)
        self.assertEqual(cl.add(-1, -2), -3)
        self.assertEqual(cl.add(1, 0), 1)
        self.assertEqual(cl.add(0, 2), 2)

        with self.assertRaises(TypeError):
            cl.add('abc', 2)
            cl.add(2, 'abc')
            cl.add(True, 2)
            cl.add(2, True)

    def test_subtract(self):
        self.assertEqual(cl.subtract(1, 2), -1)
        self.assertEqual(cl.subtract(-1, 2), -3)
        self.assertEqual(cl.subtract(1, -2), 3)
        self.assertEqual(cl.subtract(-1, -2), 1)
        self.assertEqual(cl.subtract(1, 0), 1)
        self.assertEqual(cl.subtract(0, 2), -2)
        self.assertEqual(cl.subtract(-1, -1), 0)

        with self.assertRaises(TypeError):
            cl.subtract('abc', 2)
            cl.subtract(2, 'abc')
            cl.subtract(True, 2)
            cl.subtract(2, True)

    def test_multiply(self):
        self.assertEqual(cl.multiply(1, 2), 2)
        self.assertEqual(cl.multiply(-1, 2), -2)
        self.assertEqual(cl.multiply(1, -2), -2)
        self.assertEqual(cl.multiply(-1, -2), 2)
        self.assertEqual(cl.multiply(1, 0), 0)
        self.assertEqual(cl.multiply(0, 2), 0)

        with self.assertRaises(TypeError):
            cl.multiply('abc', 2)
            cl.multiply(2, 'abc')
            cl.multiply(True, 2)
            cl.multiply(2, True)

    def test_divide(self):
        self.assertEqual(cl.divide(1, 2), 0.5)
        self.assertEqual(cl.divide(2, 1), 2)
        self.assertEqual(cl.divide(-1, 2), -0.5)
        self.assertEqual(cl.divide(1, -2), -0.5)
        self.assertEqual(cl.divide(-1, -2), 0.5)
        self.assertEqual(cl.divide(0, 2), 0)
        self.assertEqual(cl.divide(0, -2), 0)

        with self.assertRaises(ValueError):
            cl.divide(2, 0)

        with self.assertRaises(TypeError):
            cl.divide('abc', 2)
            cl.divide(2, 'abc')
            cl.divide(True, 2)
            cl.divide(2, True)

    def test_sin_as_degree(self):
        self.assertEqual(cl.sin_as_degree(0), 0)
        self.assertEqual(cl.sin_as_degree(15), 0.26)
        self.assertEqual(cl.sin_as_degree(30), 0.5)
        self.assertEqual(cl.sin_as_degree(45), 0.71)
        self.assertEqual(cl.sin_as_degree(60), 0.87)
        self.assertEqual(cl.sin_as_degree(90), 1.0)
        self.assertEqual(cl.sin_as_degree(180), -0.0)
        self.assertEqual(cl.sin_as_degree(-180), 0.0)
        self.assertEqual(cl.sin_as_degree(-90), -1.0)
        self.assertEqual(cl.sin_as_degree(-60), -0.87)
        self.assertEqual(cl.sin_as_degree(-45), -0.71)
        self.assertEqual(cl.sin_as_degree(-30), -0.5)
        self.assertEqual(cl.sin_as_degree(-15), -0.26)

        with self.assertRaises(TypeError):
            cl.sin_as_degree('abc')
            cl.sin_as_degree(True)

    def test_cos_as_degree(self):
        self.assertEqual(cl.cos_as_degree(0), 1.0)
        self.assertEqual(cl.cos_as_degree(15), 0.97)
        self.assertEqual(cl.cos_as_degree(30), 0.87)
        self.assertEqual(cl.cos_as_degree(45), 0.71)
        self.assertEqual(cl.cos_as_degree(60), 0.5)
        self.assertEqual(cl.cos_as_degree(90), -0.0)
        self.assertEqual(cl.cos_as_degree(180), -1.0)
        self.assertEqual(cl.cos_as_degree(-180), -1.0)
        self.assertEqual(cl.cos_as_degree(-90), -0.0)
        self.assertEqual(cl.cos_as_degree(-60), 0.5)
        self.assertEqual(cl.cos_as_degree(-45), 0.71)
        self.assertEqual(cl.cos_as_degree(-30), 0.87)
        self.assertEqual(cl.cos_as_degree(-15), 0.97)

        with self.assertRaises(TypeError):
            cl.cos_as_degree('abc')
            cl.cos_as_degree(True)

    def test_tan_as_degree(self):
        self.assertEqual(cl.tan_as_degree(0), 0.0)
        self.assertEqual(cl.tan_as_degree(15), 0.27)
        self.assertEqual(cl.tan_as_degree(30), 0.58)
        self.assertEqual(cl.tan_as_degree(45), 1.0)
        self.assertEqual(cl.tan_as_degree(60), 1.73)
        self.assertEqual(cl.tan_as_degree(90), -195947340017.99)
        self.assertEqual(cl.tan_as_degree(180), 0.0)
        self.assertEqual(cl.tan_as_degree(-180), -0.0)
        self.assertEqual(cl.tan_as_degree(-90), 195947340017.99)
        self.assertEqual(cl.tan_as_degree(-60), -1.73)
        self.assertEqual(cl.tan_as_degree(-45), -1.0)
        self.assertEqual(cl.tan_as_degree(-30), -0.58)
        self.assertEqual(cl.tan_as_degree(-15), -0.27)

        with self.assertRaises(TypeError):
            cl.tan_as_degree('abc')
            cl.tan_as_degree(True)

    def test_log(self):
        self.assertEqual(cl.log(1, 10), 0.0)
        self.assertEqual(cl.log(10, 2), 3.32)
        self.assertEqual(cl.log(1.2, 10), 0.08)
        self.assertEqual(cl.log(10, 1.2), 12.63)

        with self.assertRaises(ZeroDivisionError):
            cl.log(10, 1)

        with self.assertRaises(ValueError):
            cl.log(-1, 10)
            cl.log(10, -1)

        with self.assertRaises(TypeError):
            cl.log(5, 'abc')
            cl.log('abc', 5)
            cl.log(5, True)
            cl.log(True, 5)

    def test_square_root(self):
        self.assertEqual(cl.square_root(0), 0.0)
        self.assertEqual(cl.square_root(1), 1.0)
        self.assertEqual(cl.square_root(4), 2.0)
        self.assertEqual(cl.square_root(1.2), 1.095)

        with self.assertRaises(ValueError):
            cl.square_root(-2)

        with self.assertRaises(TypeError):
            cl.square_root('abc')
            cl.square_root(True)

    def test_power(self):
        self.assertEqual(cl.power(0, 2), 0.0)
        self.assertEqual(cl.power(2, 0), 1.0)
        self.assertEqual(cl.power(2, 2), 4.0)
        self.assertEqual(cl.power(2, 3.2), 9.19)
        self.assertEqual(cl.power(2.4, 1.2), 2.859)
        self.assertEqual(cl.power(2.4, 2), 5.76)

        with self.assertRaises(ValueError):
            cl.power(-2, 1.5)

        with self.assertRaises(TypeError):
            cl.power('abc', 3)
            cl.power(3, 'abc')
            cl.power(True, 3)
            cl.power(3, True)

    def test_factorial(self):
        self.assertEqual(cl.factorial(0), 1)
        self.assertEqual(cl.factorial(1), 1)
        self.assertEqual(cl.factorial(5), 120)

        with self.assertRaises(ValueError):
            cl.factorial(-2)

        with self.assertRaises(TypeError):
            cl.factorial('abc')
            cl.factorial(2.5)
            cl.factorial(True)

    def test_circle_area(self):
        self.assertAlmostEqual(cl.circle_area(1), pi)
        self.assertAlmostEqual(cl.circle_area(3), pi * 3 ** 3)
        self.assertAlmostEqual(cl.circle_area(2.4), pi * 2.4 ** 2.4)
        self.assertAlmostEqual(cl.circle_area(0.4), pi * 0.4 ** 0.4)

        with self.assertRaises(ValueError):
            cl.circle_area(-3)

        with self.assertRaises(TypeError):
            cl.circle_area('abc')
            cl.circle_area(True)


if __name__ == '__main__':
    unittest.main()
