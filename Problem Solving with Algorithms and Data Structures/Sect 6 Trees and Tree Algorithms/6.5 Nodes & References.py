class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    
    #If leftchild already exists, push the existing one down and insert the newNode as the leftchild of the root.    
    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
            
    #same with rightchild
    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t    
        
    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild
    
    def setRootVal(self,obj):
        self.key = obj
    
    def getRootVal(self):
        return self.key    
    
r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())

#same as in 6.4 but using the nodes/references implementation
def buildTree():
    tree=BinaryTree("a")
    print(tree.key)
    tree.insertLeft("b")
    print(tree.leftChild.key)
    tree.insertRight("c")
    print(tree.rightChild.key)
    tree.leftChild.insertRight("d")
    print(tree.leftChild.rightChild.key)
    tree.rightChild.insertLeft("e")
    print(tree.rightChild.leftChild.key)
    tree.rightChild.insertRight("f")
    print(tree.rightChild.rightChild.key)
    return tree
    
buildTree()