import unittest
from io import StringIO
import sys
from main import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    def capture_output(self, n):
        output = StringIO()
        sys.stdout = output
        fizzbuzz(n)
        sys.stdout = sys.__stdout__
        return output.getvalue().strip().split("\n")

    def test_fizz(self):
        output = self.capture_output(3)
        self.assertEqual(output[-1], "Fizz")

    def test_buzz(self):
        output = self.capture_output(5)
        self.assertEqual(output[-1], "Buzz")

    def test_fizzbuzz(self):
        output = self.capture_output(15)
        self.assertEqual(output[-1], "Fizzbuzz")

    def test_number(self):
        output = self.capture_output(2)
        self.assertEqual(output[-1], "2")


if __name__ == "__main__":
    unittest.main()
