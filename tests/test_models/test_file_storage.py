#!/usr/bin/python3
"""
my unittest module for base class
"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class testFileStorage(unittest.TestCase):
    """class for test basemodel methods"""
    def setUp(self):
        self.storage = FileStorage()

    def test_all(self):
        """test all function"""
        inst1 = BaseModel()
        test = self.storage.all()
        self.assertIsInstance(test, dict)
        self.assertIn(inst1, test.values())

    def test_new(self):
        """test new"""
        inst1 = BaseModel()
        self.storage.new(inst1)
        test = self.storage.all()
        self.assertIn("BaseModel." + (inst1.id), test)

    def test_save(self):
        """test save"""
        inst1 = BaseModel()
        self.storage.new(inst1)
        self.storage.save()
        file_check = os.path.exists("Airbnb.json")
        self.assertEqual(True, file_check)

    def test_reload(self):
        """test reload from file"""
        inst1 = BaseModel()
        self.storage.new(inst1)
        self.storage.save()
        self.storage.reload()
        test = self.storage.all()
        self.assertIn("BaseModel." + (inst1.id), test)
