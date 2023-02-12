#!/usr/bin/python3
"""
Unittest for user.py
"""
import unittest
from models.user import User
import datetime


class UserCase(unittest.TestCase):
    """Tests instances and methods from user class"""

    user1 = User()

    def test_class_exists(self):
        """tests if class exists"""
        string1 = "<class 'models.user.User'>"
        self.assertEqual(str(type(self.user1)), string1)

    def test_user_inheritance(self):
        """test if User is a subclass of BaseModel"""
        self.assertIsInstance(self.user1, User)

    def testHasAttributes(self):
        """check if attributes exist"""
        self.assertTrue(hasattr(self.user1, 'email'))
        self.assertTrue(hasattr(self.user1, 'password'))
        self.assertTrue(hasattr(self.user1, 'first_name'))
        self.assertTrue(hasattr(self.user1, 'last_name'))
        self.assertTrue(hasattr(self.user1, 'id'))
        self.assertTrue(hasattr(self.user1, 'created_at'))
        self.assertTrue(hasattr(self.user1, 'updated_at'))

    def test_types(self):
        """tests type of the attribute is the correct one"""
        self.assertIsInstance(self.user1.first_name, str)
        self.assertIsInstance(self.user1.last_name, str)
        self.assertIsInstance(self.user1.email, str)
        self.assertIsInstance(self.user1.password, str)
        self.assertIsInstance(self.user1.id, str)
        self.assertIsInstance(self.user1.created_at, datetime.datetime)
        self.assertIsInstance(self.user1.updated_at, datetime.datetime)

    def test_save(self):
        self.user1.save()
        self.assertNotEqual(self.user1.created_at, self.user1.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.user1), True)


if __name__ == '__main__':
    unittest.main()
