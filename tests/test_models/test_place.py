#!/usr/bin/python3
"""
my unittest module for base class
"""

import unittest
from models.place import Place


class testPlace(unittest.TestCase):
    """class for test basemodel methods"""

    def test_instances(self):
        """check for uuid, creat, update, save"""
        ins1 = Place()
        ins1.city_id = "5856"
        ins1.user_id = "987"
        ins1.name = "mars"
        ins1.save()
        self.assertNotEqual(ins1.created_at, ins1.updated_at)
        self.assertIsInstance(ins1, Place)

        self.assertNotEqual(ins1.save(), ins1.updated_at)

        str1 = ins1.to_dict()

        like_ins1 = Place(**str1)
        self.assertEqual(like_ins1.name, ins1.name)
