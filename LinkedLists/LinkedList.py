#created node class that has data and next attribute
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

#Created Linked List class
class LinkedList:
    def __init__(self):
        self.head=None

    def append_last(self,data):
        #create node first

        new_node=Node(data)
        # case 1 : empty list
        if  self.head is None:
            self.head=new_node
            return
        # case 2 : non-empty list
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node
        


    def append_first(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node


    def delete_node(self,key):
        current=self.head

        if current and current.data == key:
            self.head=current.next
            current=None
            return

        #prev variable
        prev=None
        while current and current.data != key:
            prev=current
            current=current.next

        if not current:
            print("No element found in the linked list")

        prev.next=current.next
        current=None

    def length_linked_list(self):
        current=self.head
        count=0
        while current:
            count+=1
            current=current.next
        return count 

    def print(self):
        #print linked list
        current=self.head
        while current:
            print(current.data,end="-->")
            current=current.next
        print("None")

ll=LinkedList()
ll.append_last(60)
ll.append_last(80)
ll.append_last(90)
ll.append_first(10000)
ll.append_first(900)
ll.append_first(2020)
ll.delete_node(2020)
ll.delete_node(10000)
ll.print()
print(ll.length_linked_list())












