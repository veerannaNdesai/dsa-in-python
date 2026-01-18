
class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self,key):
        h = 0
        for i in key:
            h += ord(i)
        
        return h % self.MAX
    
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        start_index = h

        while self.arr[h] is not None:
            # case 1: if key already exists
            if self.arr[h][0] == key:
                self.arr[h] = (key,val)
                return
            # case 2: if the index value is not none and the value is different one
            h = (h + 1) % self.MAX
            
            if h == start_index:
                raise Exception("Hashmap is full.")

        self.arr[h] = (key,val)

        


h1 = HashTable()
h1["march 6"] = 10
h1['march 17'] = 11
h1['march 19'] = 11
print(h1.get_hash("march 18"))
h1['march 18'] = 11
h1['march 20'] = 27
h1['march 21'] = 27
h1['march 22'] = 27
h1['march 23'] = 27
h1['march 24'] = 27
h1['march 25'] = 27
# h1['march 26'] = 27

print(h1.arr)



