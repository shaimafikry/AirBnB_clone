#!/usr/bin/python3
"""
my unittest module for base class
"""

import unittest
from models.base_model import BaseModel


class testBaseModel(unittest.TestCase):
    """class for test basemodel methods"""

    def test_instances(self):
        """check for uuid, creat, update, save"""
        ins1 = BaseModel()
        ins2 = BaseModel()
        ins1.save()
        ins1_str = str(ins1)
        self.assertNotEqual(ins1.id, ins2.id)
        self.assertNotEqual(ins1.created_at, ins1.updated_at)
        self.assertIsInstance(ins1.id, str)
        self.assertIsInstance(ins1, BaseModel)
        self.assertNotEqual(ins1.save(), ins1.updated_at)
        self.assertNotEqual(ins1_str, ins1.__str__())
        str1 = ins1.to_dict()
        str2 = ins2.to_dict()
        self.assertEqual(str1["__class__"], str2["__class__"])
        like_ins1 = BaseModel(**str1)
        self.assertEqual(like_ins1.id, ins1.id)
