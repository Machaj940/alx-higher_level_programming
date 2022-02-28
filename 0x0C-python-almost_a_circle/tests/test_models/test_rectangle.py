#!/usr/bin/python3
"""Unittest for Almost-a-Circle base class
"""
import unittest
from models import rectangle
from models.base import Base
Rectangle = rectangle.Rectangle

class Testrectangle(unittest.TestCase):

    def test_id(self):
        """Test for functioning ID"""
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 9)
        self.assertEqual(self.r4.id, 3)

    def test_width(self):
        """Test for functioning width"""
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r3.width, 5)
        self.assertEqual(self.r4.width, 11)

    def test_height(self):
        """Test for functioning height"""
        self.assertEqual(self.r1.height, 10)
        self.assertEqual(self.r2.height, 3)
        self.assertEqual(self.r3.height, 6)
        self.assertEqual(self.r4.height, 12)

    def test_x(self):
        """Test for functioning x"""
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 4)
        self.assertEqual(self.r3.x, 7)
        self.assertEqual(self.r4.x, 13)

    def test_y(self):
        """Test for functioning y"""
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r3.y, 8)
        self.assertEqual(self.r4.y, 14)
