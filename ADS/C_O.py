class Triangle():
  def __init__(self,base,height):
    self.base = base
    self.height = height
  def calculate_area(self):
    return 0.5 * self.base * self.height

t = Triangle(4,3)
print ("Area_of_Triangle", t.calculate_area())
  
  
class Student():
  def __init__(self,name,age, bf):
    self.name = name
    self.age = age
    self.bf = bf

  def change_name(self,new_name):
    self.name = new_name
    return (self.name)

  def happy_birthday(self):
    self.age += 1
    return (self.age)

  def bf_name(self):
    print(self.bf)

a = Student('alisha',19,'shraddha')
print(a.change_name('alisha'))
print(a.happy_birthday())
a.bf_name()

    