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