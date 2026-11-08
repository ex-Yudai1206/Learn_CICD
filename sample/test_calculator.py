import unittest

from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculator()

    def test_add(self) -> None:
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_subtract(self) -> None:
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiply(self) -> None:
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_divide(self) -> None:
        self.assertEqual(self.calc.divide(10, 4), 2.5)

    def test_divide_by_zero(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(1, 0)

    def test_history(self) -> None:
        self.calc.add(1, 2)
        self.calc.multiply(2, 3)
        self.assertEqual(self.calc.history, ["1 + 2 = 3", "2 * 3 = 6"])
        self.calc.clear_history()
        self.assertEqual(self.calc.history, [])


if __name__ == "__main__":
    unittest.main()
