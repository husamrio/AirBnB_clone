#!/usr/bin/python3
"""
This is a unit test for the FileStorage class
"""
import pep8
import unittest
import os
import json
from models.user import User
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
from models.engine.file_storage import FileStorage
from models.amenity import Amenity


class TestFileStorage(unittest.TestCase):
    '''File storage testing'''

    @classmethod
    def teardown(cls):
        del cls.rev1
    def teardown(self):
        try:
            os.remove("file.json")
        except:
            pass
    
    @classmethod
    def setUpClass(cls):
        cls.rev1 = Review()
        cls.rev1.place_id = "Raleigh"
        cls.rev1.user_id = "Greg"
        cls.rev1.text = "Grade A"

    def test_reload(self):
        """
        Method for tests: reload (reloads objects from string file)
        """
        a_storage = FileStorage()
        try:
            os.remove("file.json")
        except:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(a_storage.reload(), None)    
    
    def test_all(self):
        """
        Tests method: all (returns dictionary <class>.<id> : <obj instance>)
        """
        storage = FileStorage()
        instances_dic = storage.all()
        self.assertIsNotNone(instances_dic)
        self.assertEqual(type(instances_dic), dict)
        self.assertIs(instances_dic, storage._FileStorage__objects)    
    
    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_new(self):
        """
        Tests method: new (saves new object into dictionary)
        """
        m_storage = FileStorage()
        instances_dic = m_storage.all()
        hussein = User()
        hussein.id = 999999
        hussein.name = "Hussein"
        m_storage.new(hussein)
        key = hussein.__class__.__name__ + "." + str(hussein.id)
        #print(instances_dic[key])
        self.assertIsNotNone(instances_dic[key])