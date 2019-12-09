import json
from school import School

def print_deserialize():
    with open('./schooldata.json') as json_file:
        school_dict = json.load(json_file)
        school_str = json.dumps(school_dict)
        
        school = json.loads(school_str, object_hook=School.from_dict)
        
        # print students in school
        for student in school.students:
            print(f"Hello my name is {student.name}, I am {student.age} years old.")

if __name__ == "__main__":
    print_deserialize()