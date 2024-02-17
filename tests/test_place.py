#!/usr/bin/python3
"""
my unittest module for base class
"""

import unittest
from models.engine.file_storage import FileStorage
from models.place import Place


class testPlace(unittest.TestCase):
    """class for test basemodel methods"""

    def test_instance(self):
        inst1 = Place()
        inst1.city_id = "655555"
        inst1.user_id = "69551"
        inst1.name = "mercle"
        inst1.description = "heaven"
        FileStorage.new(self, inst1)
        FileStorage.save(self)
        FileStorage.reload(self)
        test = FileStorage.all(self)
        self.assertIn("Place." + (inst1.id), test)
