#!/usr/bin/python3
"""Unittest for Almost-a-Circle base class
"""
import unittest
from models import base
Base = base.Base

class Testbase(unittest.TestCase):

    def test_id_is_not_none(self):
        b = Base(4)
        self.assertEqual(b.id, 4)

    def test_no_arg(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_negative_arg(self):
        b = Base(-4)
        self.assertEqual(b.id, -4)

    def test_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            b = Base(4, 4)
