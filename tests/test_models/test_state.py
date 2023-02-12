#!/usr/bin/python3

import unittest
import os
from models.state import State
from models.base_model import BaseModel
import datetime


class TestState(unittest.TestCase):

    state1 = State()

    def test_class_exist(self):
        """ test if class is present """
        name = "<class 'models.state.State'>"
        self.assertEqual(str(type(self.state1)), name)

    def test_inheritance(self):
        """test if State is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.state1.__class__, BaseModel), True)

    def test_attributes(self):
        """ check if attributes exists """
        self.assertTrue(hasattr(self.state1, 'name'))
        self.assertTrue(hasattr(self.state1, 'id'))
        self.assertTrue(hasattr(self.state1, 'created_at'))
        self.assertTrue(hasattr(self.state1, 'updated_at'))

    def test_types(self):
        """tests type of the attribute is the correct one"""
        self.assertIsInstance(self.state1.name, str)
        self.assertIsInstance(self.state1.id, str)
        self.assertIsInstance(self.state1.created_at, datetime.datetime)
        self.assertIsInstance(self.state1.updated_at, datetime.datetime)


if __name__ == "__main__":
    unittest.main()
