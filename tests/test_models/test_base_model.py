#!/usr/bin/python3
"""
my unittest module for base class
"""

import unittest
from models.base_model import BaseModel


class testbaseMOdel(unittest.TestCase):
    """class for test basemodel methods"""

    def test_instances(self):
        """check for uuid, creat, update, save"""
        ins1 = BaseModel()
        ins2 = BaseModel()
        ins1.save()
        self.assertNotEqual(ins1.id, ins2.id)
        self.assertNotEqual(ins1.created_at, ins1.updated_at)
        self.assertIsInstance(ins1.id, str)
        self.assertIsInstance(ins1, BaseModel)
