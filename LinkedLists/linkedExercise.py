class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def append_last(self,data):
        new_node=Node(data)
        #case 1: when empty list
        if self.head == None:
            self.head=new_node
            return
        #case 2: when not empty
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node

    def append_first(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    
    def delete(self,key):

        # Case 1 : empty List
        if self.head == None:
            print("Linked List is empty")
            return

        #Case 2: head node holds the value to be deleted
        if self.head.data==key:
            self.head=self.head.next
            return

        #Case 3: Search for the node to delete
        current=self.head
        #current.next is used to check if we are at the end of the linkedList
        #current.data checks our previous data
        while current.next and current.next.data != key:
            current=current.next

        if current.next is None:
            print("element Not Found")
            return
        
        current.next=current.next.next


    def printList(self):
        current_pointer=self.head
        while current_pointer:
            print(current_pointer.data,end="-->")
            current_pointer=current_pointer.next
        print("None")

ll=LinkedList()
ll.append_last(678)
ll.append_last(78)
ll.append_last(8)
ll.append_first(1000)
ll.printList()
ll.delete(1000)
ll.printList()
ll.delete(778)
ll.printList()
