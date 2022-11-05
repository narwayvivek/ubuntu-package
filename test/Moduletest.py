import unittest

from src.ubuntu_package.module import (add, subtract, multiply, divide)


class TestModule(unittest.TestCase):
    def add(self):
        self.assertEqual(add(1, 2), 3)

    def sbtract(self):
        self.assertEqual(subtract(1, 2), -1)
    
    def multiply(self):
        self.assertEqual(multiply(1, 2), 2)
    
    def divide(self):
        self.assertEqual(divide(50, 5), 10)