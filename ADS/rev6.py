class Node():
  def __init__(self,value,next):
      self.value=value
      self.next=next
        
class Linkedlist():
  def __init__(self):
      self.head=Node(0,None)
      one=Node(1,None)
      two=Node(2,None)
      three=Node(3,None)
      four=Node(4,None)
      five=Node(5,None)
      six=Node(6,None)
      seven=Node(7,None)
      eight=Node(8,None)
      nine=Node(9,None)
        
      self.head.next=one
      one.next=two
      two.next=three
      three.next=four
      four.next=five
      five.next=six
      six.next=seven
      seven.next=eight
      eight.next=nine
      
        
  def print_list(self):
      current = self.head.next
      while (current != None):
          print(current.value)
          current = current.next
    
  def rotate(self):
      first=self.head.next
      current=first
      while(current.next!=None):
           current = current.next
      current.next = first
      self.head.next = first.next
      first.next=None
         
a = Linkedlist()
a.print_list()
print()
a.rotate()
a.print_list()
        

#Create a method rotate(self) to put the first element in the end
#So after calling rotate once, your list should be 2,3,4,5,6,7,8,9,1