# Exercise : to add insert after method-- def insert_after_data(self,insert_after,data_to_insert):


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

    def get_index_of(self,value):
        itr = self.head
        if value == self.head.data:
            return 0
        count = 0
        while itr:
            if value == itr.data:
                return count
            count += 1
            itr = itr.next
        else:
            raise Exception("Enter a valid value to get index.")



    def insert_after_data(self,insert_after,data_to_insert):

        itr = self.head

        if insert_after == self.head:
            node = Node(data_to_insert,self.head.next)
            self.head.next = node
            return
        InsertAfterIndex = self.get_index_of(insert_after)
        count = 0
        while itr:
            if count == self.get_length()-1:
                node = Node(data_to_insert,None)
                itr.next = node
                return
            if count == InsertAfterIndex:
                node = Node(data_to_insert,itr.next)
                itr.next = node
                return
            count += 1
            itr = itr.next

l1 = LinkedList()
l1.insert_values(["Veeranna","Kiran","Lohit","Mohin"])
l1.print()
l1.insert_after_data("Mohin","Naveen")
l1.print()





        
