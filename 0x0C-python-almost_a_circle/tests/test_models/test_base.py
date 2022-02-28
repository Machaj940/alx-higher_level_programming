#!/usr/bin/python3
"""Unittest for Almost-a-Circle base class
"""
import unittest
from models import base


class Testbase(unittest.TestCase):

    def test_id_is_not_none(self):
        b = Base(4)
        self.assertEqual(b.id, 4)
        
