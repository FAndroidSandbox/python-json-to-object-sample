from student import Student
from typing import List

class School:
    def __init__(self, school_name=None, students: List[Student]=None):
        self.school_name = school_name
        self.students = students

    @classmethod
    def from_dict(cls, dict):
        obj = cls()
        obj.__dict__.update(dict)
        return obj