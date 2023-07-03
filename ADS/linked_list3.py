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