class Node():
    def __init__(self,val,next):
        self.val = val
        self.next = next

#Create a single element linked list
#Node with 1 value and next = None
s = Node(1,None)
print(s.val,s.next)

s2 = Node(2,None)
print(s2.val,s2.next)                      

s.next = s2
print("Connected list:",s.val,s.next)

#print(s.next.val) #2
#print(s.next.next) #None

#Create s3 value 3 connect it to s2
s3 = Node(3, None)
s2.next = s3
print("Connected list:",s.val,s.next)
