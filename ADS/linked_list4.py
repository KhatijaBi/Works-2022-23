class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node(0)
        one = Node(1)
        two = Node(2)
        three = Node(3)

        self.head.next = one
        one.next = two
        two.next = three
        three.next = self.head

    def print_list(self):
        current = self.head.next
        while current != None:
            print(current.value)
            current = current.next

    def unlink(self):
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = None

a = LinkedList()
a.unlink()
a.print_list()
