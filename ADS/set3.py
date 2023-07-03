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