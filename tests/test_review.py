#!/usr/bin/python3
"""
my unittest module for base class
"""

import unittest
from models.engine.file_storage import FileStorage
from models.review import Review


class testReview(unittest.TestCase):
    """class for test basemodel methods"""

    def test_instances(self):
        """check for uuid, creat, update, save"""
        inst1 = Review()
        inst1.place_id = "69551"
        inst1.user_id = "65687"
        inst1.text = "text"
        FileStorage.new(self, inst1)
        FileStorage.save(self)
        FileStorage.reload(self)
        test = FileStorage.all(self)
        self.assertIn("Review." + (inst1.id), test)
