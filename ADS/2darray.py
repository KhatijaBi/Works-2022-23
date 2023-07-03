arr = [
    [1,2,3,4,5],
    [2,3,4,5,6],
    [3,4,5,6,7],
]
row = 1
column = 2
print(arr[row][column])

#Printing out the row
row = 1
print(arr[row])

for column in range(5):
    print(arr[row][column])

#Printing a column
column = 2
print(arr[column])

for row in range(3):
    print(arr[column][row])

arr = [1,2,3,4,5,6,7,8,9,10]
s=0
for i in arr:
    if i%2 ==0:
        s+=i
print(s)

arr = [1,2,3,4,5,6,7,8,9,10]
s = 0
for i in arr:
    count = 0
for j in range(2,i):
    if i%j == 0:
        count = 1
        break
    if count == 0 and i != 1:
      s+=i 
print(s)

class Fraction():
    def __init__(self,num,den):
        self.num = num
        self.den = den
f1 = Fraction(1,2)
f2  =Fraction(2,3)
print(f"fraction is (f1.num) / (f1.den)")
print(f"fraction is (f2.num)/(f2.den)")

class complex():
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary
a=complex(0,1)
b=complex(1,0)
print(a.real, a.imaginary)
print(b.real,b.imaginary)


class triangle():
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def calculate_area(self):
        return 0.5 * self.base * self.height
    
t = triangle(4,3)
print("area_of_triangle", t.calculate.area())

class Student():
    def __init__(self,name,age,bf):
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

a = Student('alisha', 19, 'shraddha')
print(a.change_name('alisha'))
print(a.happy_birthday())
a.bf_name()

class student():
    def __init__(self, name, age, section):
        self.name = name
        self.age = age
        self.section = section
    
    def get_name(self):
        return self.age
    
    def get_section(self):
        return self.section
    
s1 = student("alisha", 19, 'A')
print(f"Name = {s1.name}, Age = {s1.age},section ={s1.section}")

class student_list():
    def __init__(self,student):
        self.student=student
    
    def get_Student_name(self):
        return self.Student.name
        
    def get_Student_age(Self):
           return Self.Student.age
    
    def get_student_section(self):
        return self.student.section

student1 = student_list(student('alisha',19,'A'))
print (f"student1 attributes are: {student1.get_student_name()}, {student1.get_student_age()}, {student1.get_tudent_section()}")

class Camel():
    def __init__ (self, length, width):
        self.length = length
        self.width = width
    def find_volume(self):
        return 2 * (self.length + self.width)

camel1 = Camel(1,1)
print(camel1.find_volume())


class student():
    def __init__ (self,name,roll,best_friend):
        self.name = name
        self.roll = roll
        self.best_friend = best_friend

    def get_name(Self):
        return Self.name
    
    def get_roll(self):
        return self.roll
    
    def get_best_friend(self):
        return self.get_best_friend
    
student1 = student("alish", 19, "rosh")
student2 = student("affu", 26, "alish")

if student1.get_best_friend() == student2.get_name():
    print("true")
else:
    print("false")

class node():
    def __init__(self,val,next):
        self.val = val
        self.next = next

s = node(1, None)
print(s.val,s.next)

s2 = node(2,None)
print(s.val,s.next)

s.next = s2
print("connected list:",s.val,s.next)

s3 = node(3, None)
s2.next = s3
print("connected list:",s.val,s.next)

class Node():
    def __init__ (self, value, next):
        self.value = value
        self.next = next

class LinkedList():
    def __init__ (self):
        self.head = Node(0,None)
        self.one = Node(1,None)
        self.two = Node(2,None)
        self.three = Node(3,None)

        self.head.next = self.one
        self.one.next = self.two
        self.two.next = self.three

    def print_list(self):
        current_node = self.head.next
        print(current_node.value)
        print(current_node.next.value)
        print(current_node.next.value)

    def largest(self):
        current_node = self.head.next
        largest_value = current_node.value
        if(current_node.value>largest_value):

def find_max():
    list = [1,2,3,4]
    max = 0
    for i in list:
        if(i>max):
            max = i
    return max
print (find_max())

class Node():
    def __init__(self,val,next):
        self.val = val
        self.next = next

class Linkedlist():
    def __init__(self):
        self.head=Node(0,None)
        self.one=Node(1,None)
        self.two=Node(2,None)
        self.three=Node(3,None)

        self.head.next= self.one
        self.head.next = self.two
        self.head.next = self.three

    def find_max(self):
        current = self.head.next
        max = self.head.value
        while (current!=None):
            if(current.value > max):
                max = current.value
                current = current.next
        return max
    
a=Linkedlist()
print(a.find_max())


class Node():
    def __init__(self,val,next)
        self.val = val
        self.next = next
class LinkedList():
    def __init__(self):
        self.head = Node(0,None)
        current = self.head
        for i in range(1,4):
            current.next=Node(i,None)
            current = current.next

    def find_second_largest(self):
      current = self.head.next
      largest = self.head.value
      second_largest = self.head.value
      while(current!=None):
        if(current.value > largest):
            second_largest = largest
            largest = current.value
        if(current.value < largest and current.value > second_largest):
            second_largest = current.value
        current = current.next
      print(f"the first largest no. in linked list is {largest}")
      print(f"the second largest no. in linked list is {second_largest}")

a = LinkedList()
a.find_second_largest()

def find_sum(arr):
  sum=0
  for i in arr:
    if(i%2 == 0):
     sum = sum + i
  return sum

arr=[1,2,4,6,8,9]
print(find_sum(arr))

class Node():
  def __init__(self, value, next):
    self.value=value
    self.next=next

class Linkedlist():
  def __init__(self):
    self.head=Node(0,None)
    current=self.head
    
    for i in range(1,5):
      current.next= Node(i,None)
      current=current.next

  def find_sum2(self):
    sum=0
    current = self.head.next
    while(current!=None):
      if(current.value %2 == 0):
       sum = sum + current.value
      current = current.next
    return sum

list1=Linkedlist()
print(list1.find_sum2())

num = int(input("Enter a value: "))
for i in range(1,num):
 print(i, end =" ")
print()

for i in range(1,num):
  print(1-i, end=" ")
print()

for i in range(num * 2):
  sum = 0
  if(i%2 == 0):
    continue
  else:
    print(i, end=" ")
print()

for i in range(9,-4,-3):
  print(i,end=" ")
print()

num = int(input("Enter the number of stars: "))
for i in range(1, num+1):
   print(' '* (num-i) + '*' *(2*i-1))

#Write a python function to find sum of all the numbers greater than 2 in a given list
def func1(arr):
    total = 0
    for num in arr:
        if num > 2:
            total += num
    return total

arr = [1, 2, 3, 4, 5, 6]
print(func1(arr))

#Write a python function to replace all " 2 s" in a given  list by "0 s"

def func2(arr):
    for i in range(len(arr)):
        if arr[i] == 2:
            arr[i] = 0

arr = [2, 2, 3, 4, 5]
func2(arr)
print(arr)

#Write a python function to get all the even numbers within the range (0,n) where n is given by the user. Then add one to the result and return a list:
def func3(n):
    even_numbers = []
    for i in range(0, n+1, 2):
        even_numbers.append(i + 1)
    return even_numbers

print(func3(8))

class Node():
    def __init__(self,value,next):
        self.value=value
        self.next=next
class linkedlist():
    def __init__(self):
        self.head=Node(0,None)
        one=Node(1,None)
        two=Node(2,None)
        three=Node(2,None)
        four=Node(3,None)
        five=Node(3,None)
        six=Node(4,None)
        
        self.head.next=one
        one.next=two
        two.next=three
        three.next=four
        four.next=five
        five.next=six        
    def print_list(self):
        current=self.head.next
        while current is not None:
            print(current.value)      
            current=current.next 
    
    def search_node(self,value):
        current=self.head.next 
        while current is not None:
          if current.value==value:
            print(current.value) 
        current=current.next
        
ll=linkedlist()
ll.print_list()    
ll.search_node(4)    
ll.print_list()



class Node():
    def __init__ (self, value, next):
        self.value = value
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = Node(0,None)
        self.one = Node(1,None)
        self.two = Node(2,None)
        self.three = Node(3,None)

        self.head.next = self.one
        self.one.next = self.two
        self.two.next = self.three

    def print_list(self):
        current_node = self.head.next
        print(current_node.value)
        print(current_node.next.value)
        print(current_node.next.next.value)

    def largest(self):
        current_node = self.head.next
        largest_value = current_node.value
        if(current_node.value>largest_value):
            largest_value = current_node.value
        if(current_node.next.value>largest_value):
            largest_value = current_node.next.value
        if(current_node.next.next.value>largest_value):
            largest_value = current_node.next.next.value
        print(largest_value)

    def sum(self):
            current_node = self.head.next
            sum_node = current_node.value+current_node.next.value+current_node.next.next.value
            print(sum_node)

    def product(self):
        current_node = self.head.next
        product_node = current_node.value * current_node.next.value * current_node.next.next.value
        print(product_node)

a = LinkedList()
a.print_list()
print()
a.largest()
print()
a.sum()
print()
a.product()






class Node():
    def __init__ (self, value, next):
        self.value = value
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = Node(0,None)
        self.one = Node(1,None)
        self.two = Node(2,None)
        self.three = Node(3,None)

        self.head.next = self.one
        self.one.next = self.two
        self.two.next = self.three

    
    def print_list(self):
        current = self.head.next
        while(current!=None):
            print(current.value)
            current = current.next
            continue
        

    def print_largest(self):
        current = self.head.next
        largest = current.value
        while(current!=None):
            if(current.value>largest):
              largest =  current.value
            current = current.next
            continue

        print(f"Largest is: {largest}")

    def print_sum(self):
        current = self.head.next
        sum  = 0
        while(current!=None):
            sum += current.value
            current = current.next
            continue

        print(f"Sum is: {sum}") 

    def print_product(self):
        current = self.head.next
        product = 1
        while(current!=None):
            product *= current.value
            current = current.next
            continue

        print(f"Product is: {product}")


a = LinkedList()
a.print_list()
a.print_largest()
a.print_sum()
a.print_product()


class Node():
    def __init__ (self, value, next):
        self.value = value
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = Node(0,None)
        one = Node(1,None)
        two = Node(2,None)
        three = Node(3,None)

        self.head.next = one
        one.next = two
        two.next = three

    def append_end(self):
        new_node = Node(4, None)
        current = self.head
        while(current.next != None):
            current = current.next
        current.next = new_node

    def append_begin(self):
        new_node = Node(5,None)
        new_node.next = self.head.next
        self.head.next = new_node

    def search_node(self,value):
        current = self.head.next
        while(current != None):
            if(current.value == value):
                return True
            current = current.next
        return False
    
    def print_list(self):
        current = self.head.next
        while(current != None):
            print(current.value)
            current = current.next

a = LinkedList()
a.append_end()
a.append_begin()
a.print_list()
print(a.search_node(4))