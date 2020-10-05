import unittest
import json
import os

from app.school import School

class TestSerializesDeserialize(unittest.TestCase):
    def test_serialize(self):
        with open("test/data/schooldata.json") as json_file:
            school_dict = json.load(json_file)
            school_str = json.dumps(school_dict)
            
            school = json.loads(school_str, object_hook=School.from_dict)
            
            # Assertions
            self.assertEqual(school.school_name, "My School")
            self.assertEqual(len(school.students), 2)
            self.assertEqual(school.students[0].name, "Andy")