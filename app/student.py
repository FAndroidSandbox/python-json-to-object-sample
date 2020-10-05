class Student:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    @classmethod
    def from_dict(cls, dict):
        obj = cls()
        obj.__dict__.update(dict)
        return obj