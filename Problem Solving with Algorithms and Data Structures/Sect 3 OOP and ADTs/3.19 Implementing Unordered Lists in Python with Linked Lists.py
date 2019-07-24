class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext
        
class UnorderedList:

    def __init__(self):
        self.head = None
        self.tail = None
        
    def isEmpty(self):
        return self.head == None 
    
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        if temp.next is None:
            self.tail=temp
        
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
    
        return count    
    
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
    
        return found    
    
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
    
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext()) 
    
    def append(self, item):
        self.tail.next=Node(item)
        self.tail=self.tail.next
    
    def insert(self, item, position):
        current=self.head
        count=0
        while position > count:
            previous=current
            current=current.next
            count+=1
        if count>0:
            previous.next=Node(item)
            Node(item).next=current
        else:
            self.head=Node(item)
            self.head.next=current
            
    def index(self, item):
        current=self.head
        count=0
        while current.data!=item:
            current=current.next
            count+=1
        return count
    
    def pop(self):
        current=self.head
        while current.next is not None:
            previous=current
            current=current.next
        previous.next=None
        return current.data
                   
mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)