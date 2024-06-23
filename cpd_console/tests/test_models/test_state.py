#!/usr/bin/python3
"""
my unittest module for base class
"""

import unittest
from models.engine.file_storage import FileStorage
from models.state import State


class testState(unittest.TestCase):
    """class for test basemodel methods"""

    def test_instances(self):
        """check for uuid, creat, update, save"""
        inst1 = State()
        inst1.name = "egypt"
        FileStorage.new(self, inst1)
        FileStorage.save(self)
        FileStorage.reload(self)
        test = FileStorage.all(self)
        self.assertIn("State." + (inst1.id), test)
