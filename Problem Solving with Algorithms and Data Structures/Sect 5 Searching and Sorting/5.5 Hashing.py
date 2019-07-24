#Folding method
#Divides item into equal-size pieces (last piece excluded at times)

#Mid-square method
#Square the item, then extract some portion of the resulting digits. 

#string hashing
def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])

    return sum%tablesize

#Ways to resolve collisions
#Open addressing/Linear Probing
#Start at original hash value and places conflicting object in the next available slot. 
#Disadvantaged due to clustering, as more slots will have to be traversed needlessly to find slots for other collisions.
#Collisive items can be more evenly distributed by increasing the number of slots skipped in every check. 
#Resolving collisions=Rehashing.

#Quadratic probing
#Uses a rehash function that increments the hash value by 1, 3, 5, 7...

#Yet another more "neat" method to handling collisions
#Chaining
#Allows many items to exist at the same location in the hash table, such as having nested lists. 

#The MAP ADT
class HashTable:
    def __init__(self):
        self.size=11
        self.slots=[None]*self.size
        self.data=[None]*self.size
        
    def put(self, key, data):
        hashvalue=self.hashfunction(key, len(self.slots))
        
        if self.slots[hashvalue]==None:
            self.slots[hashvalue]=key
            self.data[hashvalue]=data
        else:
            if self.slots[hashvalue]==key:
                self.data[hashvalue]=data
            else:
                nextslot=self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot]!=None and self.slots[nextslot]!=key:
                    nextslot=self.rehash(nextslot, len(self.slots))
            
                if self.slots[nextslot]==None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
                else:
                    self.data[nextslot]=data
    
    def hashfunction(self, key, size):
        return key%size
    
    def rehash(self, oldhash, size):
        return (oldhash+1)%size
    
    def get(self, key):
        startslot=self.hashfunction(key, len(self.slots))
        
        data=None
        stop=False
        found=False
        position=startslot
        while self.slots[position]!=None and not found and not stop:
            if self.slots[position]==key:
                found=True
                data=self.data[position]
            else:
                position=self.rehash(position, len(self.slots))
                if position==startslot:
                    stop=True
        return data
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, data):
        self.put(key, data)
        