'''
implementing the hashtable using python class and object
and understanding how the dictionary works in python under the hood
'''

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self,key):
        h = 0
        for i in key:
            h += ord(i)
        
        return h % self.MAX
    
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        print(h)
        for idx,element in enumerate(self.arr[h]):
            if len(element)== 2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                return
        self.arr[h].append((key,val))
    
    def __getitem__(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        for idx,element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h].pop(idx)
                return
    
h1 = HashTable()
h1["march 10"]= 100
h1["march 6"] = 90
h1["march 17"] = 570
print(h1.arr)
del h1["march 10"]
print(h1.arr)


        