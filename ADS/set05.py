class Node():
    def __init__(self,value,next):
        self.value=value
        self.next=next
class linkedlist():
    def __init__(self):
        self.head=Node(0,None)
        one=Node(1,None)
        two=Node(2,None)
        three=Node(2,None)
        four=Node(3,None)
        five=Node(3,None)
        six=Node(4,None)
        
        self.head.next=one
        one.next=two
        two.next=three
        three.next=four
        four.next=five
        five.next=six        
    def print_list(self):
        current=self.head.next
        while current is not None:
            print(current.value)      
            current=current.next 
    
    def search_node(self,value):
        current=self.head.next 
        while current is not None:
          if current.value==value:
            print(current.value) 
        current=current.next
        
    # def delete_dup(self):
    #     current=self.head.next
    #     while current is not None:
    #         if current.value==current.next.value:
    #             current.next=current.next.next
    #         else:
                # current=current.next
                
        
ll=linkedlist()
ll.print_list()    
ll.search_node(4)  
# ll.delete_dup()      
ll.print_list()