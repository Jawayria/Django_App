from unittest import TestCase

# Create your tests here.
from pytest import raises


def divide(num1, num2):
    return num1/num2


class TestDivideByZero(TestCase):
    def test_division(self):
        self.assertRaises(ZeroDivisionError, divide, 2, 0)
