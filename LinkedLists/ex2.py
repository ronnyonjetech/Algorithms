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
        #non-empty we iterate
        current=self.head
        while current.next:
            current=current.next
        current.next=node
    
    def append_first(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node

    def delete_node(self,data):
       #when list is empty
       if self.head is None:
         print("List is empty")
         return
       #element found in the head
       if self.head.data == data:
         self.head=self.head.next
         return
       #others
       current=self.head
       while current.next and current.next.data != data:
         current=current.next

       if current.next is None:
         print("element not found")
         return
       
       current.next=current.next.next
    
    def delete_middle_node(self):
      fast=self.head
      slow=self.head
      prev=None

      while fast and fast.next:
        prev=slow
        slow=slow.next
        fast=fast.next.next
      prev.next=slow.next
      return self.head

    def printLinkedList(self):
        current=self.head
        while current:
            print(current.data,end="-->")
            current=current.next
        print("None")

ll=LinkedList()
ll.append_last(90)
ll.append_last(900)
ll.append_last(9000)
ll.append_first(484)
ll.append_first(64)
ll.delete_middle_node()
# ll.delete_node(64)
ll.printLinkedList()