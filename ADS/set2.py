def find_second_largest(arr):
    largest = arr[0]
    second_largest= arr[0]
    for i in arr:
        if i>largest:
            second_largest =largest
            largest = i
    for i in arr:
       if(i>second_largest and i!=largest):
          second_largest = i
       if(second_largest == largest):
          second_largest = i
    return second_largest

print(find_second_largest([6,1,2,3,4,5]))


class Node():
  def __init__(self, value, next):
    self.value=value
    self.next=next

class LinkedList():
   def __init__(self):
      self.head = Node(0, None)
      current = self.head
      for i in range(1,4):
         current.next = Node(i, None)
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