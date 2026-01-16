'''
Implementation of Linked List using Python
'''
class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node

    def print(self):
        if self.head == None:
            print("List is Empty")
            return
        
        itr = self.head
        listr = ""
        while itr:
            listr += str(itr.data) + "-->"
            itr = itr.next
        
        print(listr)

l1 = LinkedList()

l1.insert_at_beginning(10)
l1.insert_at_beginning(20)
l1.insert_at_beginning(30)
l1.print()

