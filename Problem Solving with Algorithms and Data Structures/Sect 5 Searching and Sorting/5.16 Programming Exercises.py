import random
"ONE"
#experiment to test the difference between sequential and binary search
def orderedSequentialSearch(alist, item):
    pos=0
    found=False
    stop=False
    while pos<len(alist) and not found and not stop:
        if alist[pos]==item:
            found=True
        else:
            if alist[pos]>item:
                stop=True
            else:
                pos+=1
    
    return found

def binarySearch(alist, item):
    first=0
    last=len(alist)-1
    found=False
    
    while first<=last and not found:
        midpoint=(first+last)//2
        if alist[midpoint]==item:
            found=True
        else:
            if item<alist[midpoint]:
                last=midpoint-1
            else:
                first=midpoint+1
    return found

def list_generator():
    l=[]
    rng=random.Random()
    length=rng.randrange(200000, 300000)
    for term in range(length):
        obj=rng.randrange(10, 400000)
        l.append(obj)
    l.sort()
    return l

def binary_vs_sequence():
    import time
    determiner=random.Random()
    for i in range(10):
        test=list_generator()
        item=determiner.randrange(10, 400000)
        bintime=time.time()      
        binarySearch(test, item)
        btime=time.time()
        print("Binary " + str(i), ": " +  repr(btime-bintime))
        seqtime=time.time()
        orderedSequentialSearch(test, item)
        stime=time.time()
        print("Sequential " + str(i), ": " + repr(stime-seqtime))

#binary_vs_sequence()
 
#As expected, the binary search is always faster than the ordered sequential search. 

"TWO"
#Test between iterative and recursive binary search
def recursiveBinarySearch(alist, item):
    if len(alist)==0:
        return False
    else:
        midpoint=len(alist)//2
        if alist[midpoint]==item:
            return True
        else:
            if item<alist[midpoint]:
                return binarySearch(alist[:midpoint], item)
            else:
                return binarySearch(alist[midpoint+1:], item)

def recursiveBinarySearch(alist, item, start, end):
    midpoint=start+(end-start)//2
    if alist[midpoint]==item:
        return True
    elif midpoint==end-1 or midpoint==start-1:
        return False    
    else:
        if item<alist[midpoint]:
            return recursiveBinarySearch(alist, item, start, midpoint)
        else:
            return recursiveBinarySearch(alist, item, midpoint+1, end)           
def binary_mashup():
    import time
    determiner=random.Random()
    for i in range(10):
        test=list_generator()
        item=determiner.randrange(10, 400000)
        itrtime=time.time()      
        binarySearch(test, item)
        itime=time.time()
        print("Iterative Binary " + str(i+1), ": " +  repr(itrtime-itime))
        rectime=time.time()
        recursiveBinarySearch(test, item, 0, len(test))
        rtime=time.time()
        print("Recursive Binary " + str(i+1), ": " + repr(rtime-rectime))

#binary_mashup()
#My experiment shows that while the book's version of recursive binary searching is faster than ordered sequential searching, it is still slower than iterative binary searching. This is most likely as this version of recursive binary needs to slice the list. 

"THREE"
#Recursive Binary Search without slicing. 
def recursiveBinarySearch(alist, item, start, end):
    midpoint=start+(end-start)//2
    if alist[midpoint]==item:
        return True
    elif midpoint==end-1 or midpoint==start-1:
        return False    
    else:
        if item<alist[midpoint]:
            return recursiveBinarySearch(alist, item, start, midpoint)
        else:
            return recursiveBinarySearch(alist, item, midpoint+1, end)
     
def rbsBenchmark():
    import time
    determiner=random.Random()
    for i in range(10):
        test=list_generator()
        item=determiner.randrange(10, 400000)
        rectime=time.time()
        recursiveBinarySearch(test, item, 0, len(test))
        rtime=time.time()
        print("Recursive Binary " + str(i+1), ": " + repr(rtime-rectime))

#rbsBenchmark()


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
        
    def __len__(self):
        length=0
        for i in self.slots:
            if i is not None:
                length+=1
        return length
    def __contains__(self, item):
        return item in self.slots
    def __delitem__(self, item):
        self.data.remove(self.data[self.slots.index(item)])
        self.slots.remove(item)

"FOUR"
#len function for HashTable
def __len__(self):
    length=0
    for i in self.slots:
        if i is not None:
            length+=1
    return length

table=HashTable()
table[12]=15
table[23]=1
#print(table.slots) 
#print(table.data)  

"FIVE"
#in function for HashTable
def __contains__(self, item):
    return item in self.slots

#print(15 in table)

"SIX"
#del method for HashTable, assuming HashTable uses open addressing.
def __delitem__(self, item):
    self.data.remove(self.data[self.slots.index(item)])
    self.slots.remove(item)
del table[12]
#print(table.slots)
#print(table.data)

"SEVEN"




