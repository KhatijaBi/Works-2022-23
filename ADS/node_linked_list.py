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