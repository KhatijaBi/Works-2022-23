#1.
class Camel():
    def __init__ (self, length, width):
        self.length = length
        self.width = width

    def find_volume(self):
        return 2 * (self.length + self.width)
    

camel1 = Camel(1,1)
print(camel1.find_volume())

#2.
class Camel_list():
    def __init__ (self, Camel):
        self.Camel = Camel

    def get_camel_volume(self):
        return self.Camel.find_volume()
    
Camel1 = Camel_list(Camel(1,1))
print(f"the volume of the camel is {Camel1.get_camel_volume()}")   


#3.
class Student():
    def __init__ (self, name, roll, best_friend):
        self.name = name
        self.roll = roll
        self.best_friend = best_friend

    def get_name(self):
        return self.name
    
    def get_roll(self):
        return self.roll
    
    def get_best_friend(self):
        return self.best_friend

student1 = Student('Alish', 29, 'Rosh')
student2 = Student('Affu', 26, 'Alish')

if student1.get_best_friend() == student2.get_name():
    print("True")

else:
    print('False')

#4. Student list problem
# class Student_List():
#     def __init__ (self, Student1,Student2):
#         self.Student1 = Student1
#         self.Student2 = Student2

#     def find_equality(self):
#         if(self.Student1.get_best_friend() == self.Student2.get_best_friend()):
#             return True
#         else:
#             return False        

# Student1 = Student('Alish', 29, 'Rosh')
# Student2 = Student('Rosh', 26, 'Affu')
# st_list = Student_List(Student1, Student2)

# print(st_list.find_equality())
