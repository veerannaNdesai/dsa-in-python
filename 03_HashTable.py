'''
implementing the hashtable using python class and object
and understanding how the dictionary works in python under the hood
'''

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self,key):
        h = 0
        for i in key:
            h += ord(i)
        
        return h % self.MAX
    
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val
    
    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None
    
o = HashTable()
o["Veeranna"] = "Killer"
print(o.arr)
print(o["Veeranna"])
del o["Veeranna"]
print(o.arr)


        