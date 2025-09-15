class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def append_last(self,data):
        node=Node(data)
        #empty
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
        if self.head is None:
            self.head=node
            return
        node.next=self.head
        self.head=node

    def delete_node(self,data):
        #empty
        if self.head is None:
            print("List is empty")
            return
        #at the first node
        if self.head.data == data:
           self.head=self.head.next
           return
        #non-empty
        current=self.head
        while current.next and current.next.data != data:
            current=current.next

        if current.next is None:
            print("element not found")
            return

        current.next=current.next.next

    def delete_middle_node(self):
    #we used 2-pointer technique fast pointer moves two steps slow pointer moves one step
      fast=self.head
      slow=self.head
      prev=None
    #when fast reaches the end the slow pointer will be pointing in the middle node
    #since prev pointer kept previous state of slow pointer we can now delete the middle node easily
      while fast and fast.next:
        prev=slow
        slow=slow.next
        fast=fast.next.next
      prev.next=slow.next
      return self.head
      
        
    def print_list(self):
        current=self.head
        while current:
            print(current.data,end="-->")
            current=current.next
        print("None")


linkedList=LinkedList()
linkedList.append_last(200)
linkedList.append_last(700)
linkedList.append_last(900)
linkedList.append_first(10)
# linkedList.delete_node(10)
linkedList.delete_middle_node()
linkedList.print_list()
