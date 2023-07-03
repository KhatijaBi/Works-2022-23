#1.
class Student():
    def __init__ (self, name, age, section):
        self.name = name
        self.age = age
        self.section = section

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_section(self):
        return self.section
    
s1 = Student('Alisha',19, 'A')
print(f"Name = {s1.name}, age = {s1.age}, section = {s1.section}")

#2.
class Student_List():
    def __init__ (self, Student):
        self.Student = Student

    def get_student_name(self):
        return self.Student.name
    
    def get_student_age(self):
        return self.Student.age
    
    def get_student_section(self):
        return self.Student.section
    
student1 = Student_List(Student('Alisha', 19, 'A'))
print(f"Student1 attributes are: {student1.get_student_name()}, {student1.get_student_age()}, {student1.get_student_section()}")



