#!/usr/bin/python3
"""
my unittest module for base class
"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class testbaseMOdel(unittest.TestCase):
    """class for test basemodel methods"""

    def test_all(self):
        """test all function"""
        inst1 = BaseModel()
        test = FileStorage.all(self)
        self.assertIsInstance(test, dict)
        self.assertIn(inst1, test.values())

    def test_new(self):
        """test new"""
        inst1 = BaseModel()
        FileStorage.new(self, inst1)
        test = FileStorage.all(self)
        self.assertIn("BaseModel." + (inst1.id), test)

    def test_save(self):
        """test new"""
        inst1 = BaseModel()
        FileStorage.new(self, inst1)
        FileStorage.save(self)
        file_check = os.path.exists("Airbnb.json")
        self.assertEqual(True, file_check)

    def test_reload(self):
        """test reload from file"""
        inst1 = BaseModel()
        FileStorage.new(self, inst1)
        FileStorage.save(self)
        FileStorage.reload(self)
        test = FileStorage.all(self)
        self.assertIn("BaseModel." + (inst1.id), test)
