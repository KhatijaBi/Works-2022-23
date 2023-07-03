class Node():
  def __init__(self,value, next):
    self.value = value
    self.next=next

class Stack():
  def __init__(self):
    self.head=Node(0,None)

  def push(self, value):
    node=Node(value, None)
    node.next = self.head.next
    self.head.next = node

  def pop(self):
    if(self.head.next == None):
      print("Stack underflow")
      return None
    else:
      stack_pop= self.head.next.value
      self.head.next = self.head.next.next
      return stack_pop
      

  def print_stack(self):
      current=self.head.next
      while(current!=None):
        print(current.value)
        current = current.next
       
s=Stack()
print("PUSH OPERATION")
s.push(1)
s.push(2)
s.push(3)
s.print_stack()
print("POP OPERATION")
s.pop()
s.print_stack()