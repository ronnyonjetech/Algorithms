class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None


    def append_last(self,data):
        node=Node(data)
        #empty linked list
        if self.head is None:
            self.head=node
            return
        
        #non-empty
        current=self.head
        while current.next:
            current=current.next

        current.next=node

    def append_first(self,data):
        node=Node(data)
        #empty
        if self.head is None:
            self.head=node
            return
        #non empty
        node.next=self.head
        self.head=node

    def delete_middle(self):
        #use two pointers

        fast=self.head
        slow=self.head
        prev=None

        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next

        prev.next=slow.next

        return self.head
    
    def delete_node(self,data):
        #empty
        if self.head is None:
            return None
        
        #on the head node
        if self.head.data == data:
            self.head=self.head.next
            return
        
        #non-empty
        current=self.head
        while current.next and current.next.data != data:
            current=current.next

        current.next=current.next.next
        

    def odd_even(self):

        if self.head is None:
            return None
        
        elif self.head.next is None:
            return self.head
        
        odd=self.head
        even=self.head.next

        even_head=even

        while even and even.next:

            odd.next=odd.next.next
            odd=odd.next

            even.next=even.next.next
            even=even.next
            
        odd.next=even_head
        return self.head

    def reverse_list(self):
        current=self.head
        previous=None

        while current:
            temp=current.next
            current.next=previous
            previous=current
            current=temp
        self.head=previous

        return self.head
    
    def print(self):
        current=self.head
        while current:
            print(current.data,end="-->")
            current=current.next
        print("None")


ll=LinkedList()
ll.append_last(90)
ll.append_last(290)
ll.append_last(390)
ll.append_last(590)
ll.append_first(10000)
ll.print()
ll.odd_even()
ll.delete_middle()
ll.delete_node(90)
ll.print()
ll.reverse_list()
print("reversed list")
ll.print()
