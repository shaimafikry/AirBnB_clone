#!/usr/bin/python3
"""
my unittest module for base class
"""

import unittest
from models.engine.file_storage import FileStorage
from models.user import User


class testUser(unittest.TestCase):
    """class for test basemodel methods"""

    def test_instances(self):
        """check for uuid, creat, update, save"""
        inst1 = User()
        inst1.email = "ahmedmostafa@alx.com"
        inst1.first_name = "ahmed"
        inst1.password = "123456"
        inst1.last_name = "mostafa"
        FileStorage.new(self, inst1)
        FileStorage.save(self)
        FileStorage.reload(self)
        test = FileStorage.all(self)
        self.assertIn("User." + (inst1.id), test)
