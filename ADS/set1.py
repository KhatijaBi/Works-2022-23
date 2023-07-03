def find_max():
  list=[1,2,3,4,5,10]
  max = 0
  for i in list:
    if(i>max):
      max = i
  return max
print (find_max())

class Node():
  def __init__(self, value, next):
    self.value=value
    self.next=next

class Linkedlist():
  def __init__(self):
    self.head=Node(0,None)
    one=Node(1,None)
    two=Node(2, None)
    three=Node(3, None)

    self.head.next=one
    one.next=two
    two.next=three

  def find_max(self):
    current = self.head.next
    max = self.head.value
    while(current!=None):
      if(current.value > max):
        max = current.value
        current = current.next
    return max

a=Linkedlist()
print(a.find_max())