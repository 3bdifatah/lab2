from dataclasses import dataclass
#student dataclass with name, id and gpa
@dataclass
class Student:
    name: str
    school_id: str
    gpa: float


student1 = Student('alex', '098qwe', 4.0)
student2 = Student('Abdifatah', '145zxc', 3.6) 
student3 = Student('awali', '123abc', 2.6)

print(student1)
print(student2)
print(student3)