'''
Implementation of Linked List using Python
'''
# Node class with data and pointer
class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next


# linked list class with different linkedlist methods
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
    
    def insert_at_the_end(self,data):
        if self.head is None:
           node = Node(data,None)
           self.head = node
           return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)

    def insert_values(self,data):
        self.head = None
        for i in data:
            self.insert_at_the_end(i)
        return
    
    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count += 1
        return count
    
    def delete_at_position(self,position):
        if position < 0 or position >= self.get_length():
            raise Exception("invalid position")
        
        if position == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head

        while itr:
            if count == position-1:
                itr.next = itr.next.next
                return
            count += 1
            itr = itr.next



    def insert_at(self,value,position):
        if value == '' or position < 0 or position >= self.get_length():
            raise Exception('Invalid Position or Value')
        elif position == 0:
            self.insert_at_beginning(value)
        elif position == self.get_length()-1:
            self.insert_at_the_end(value)
        else:
            count = 0
            itr = self.head
            while itr:
                if count == position-1:
                    node = Node(value,itr.next)
                    itr.next = node
                    break
                count += 1

    def delete_value(self,value):

        itr = self.head
        count = 0
        while itr:
            if itr.data == value:
                break
            itr = itr.next
            count += 1
        else:
            raise Exception("Invalid value entered")
        self.delete_at_position(count)
    
    # def insert_after_data(self,insert_after,data_to_insert):

        

l1 = LinkedList()

l1.insert_values(["Ban","Van","Can","Man"])
# print(l1.get_length())
# l1.delete_at_position(0)
# l1.print()
# l1.insert_at("dan",1)
l1.print()

l1.delete_value("Man")
l1.print()

# l1.insert_at_beginning(10)
# l1.insert_at_beginning(30)
# l1.print()
# l1.insert_at_the_end(40)
# l1.print()





