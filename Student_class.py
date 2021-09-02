#created student class and iniated it's attributes
class Student:
    def __init__(self, name, school_id, gpa):
        self.name = name
        self.school_id = school_id
        self.gpa= gpa

#formats string
    def __str__(self):
        print("{:<10} {:<10} {:<10}".format("Name", "ID", "GPA"))
        return("{:<10} {:<10} {:<10}\n".format(self.name, self.school_id, self.gpa))


student1 = Student('alex', '098qwe', 4.0)
student2 = Student('Abdifatah', '145zxc', 3.6) 
student3 = Student('awali', '123abc', 2.6)

print(student1)
print(student2)
print(student3)