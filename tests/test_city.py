#!/usr/bin/python3
"""
my unittest module for base class
"""
import unittest
from models.engine.file_storage import FileStorage
from models.city import City


class testCity(unittest.TestCase):
    """class for test basemodel methods"""

    def test_instances(self):
        """check for uuid, creat, update, save"""
        ins1 = City()
        ins2 = City()
        ins1.name = "Cairo"
        ins1.state_id = "528"
        ins2.name = "mars"
        ins2.state_id = "523"
        ins2.save()
        self.assertNotEqual(ins1.id, ins2.id)
        self.assertNotEqual(ins1.created_at, ins1.updated_at)
        self.assertIsInstance(ins1, City)
        self.assertNotEqual(ins1.save(), ins1.updated_at)
        str1 = ins1.to_dict()
        str2 = ins2.to_dict()
        self.assertEqual(str1["__class__"], str2["__class__"])
        like_ins1 = City(**str1)
        self.assertEqual(like_ins1.name, ins1.name)
        test = FileStorage.all(self)
        self.assertIn("City." + (ins1.id), test)
