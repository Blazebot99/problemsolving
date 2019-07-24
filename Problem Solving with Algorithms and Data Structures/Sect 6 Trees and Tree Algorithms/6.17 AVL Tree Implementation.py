#AVL trees are very similar to BSTs, except for how they keep the tree "in balance" at any given time. 

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()
    
    def __setitem__(self,k,v):
        self.put(k,v)
        
    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1
    
    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                    self._put(key,val,currentNode.leftChild)
            else:
                    currentNode.leftChild = TreeNode(key,val,parent=currentNode)
                    self.updateBalance(currentNode.leftChild)
        else:
            if currentNode.hasRightChild():
                    self._put(key,val,currentNode.rightChild)
            else:
                    currentNode.rightChild = TreeNode(key,val,parent=currentNode)
                    self.updateBalance(currentNode.rightChild)
    
    #updateBalance is a recursive call made to repeatedly recalculate the balance of the trees until one of 2 base cases are met:
    #1. The recursion function has reached the root.
    #2. The balance factor of the parent has reached 0 (note that once this happens the rest of the tree's balance will not be impacted). 
    def updateBalance(self,node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        if node.parent != None:
            if node.isLeftChild():
                    node.parent.balanceFactor += 1
            elif node.isRightChild():
                    node.parent.balanceFactor -= 1
    
            if node.parent.balanceFactor != 0:
                    self.updateBalance(node.parent)
                    
    #Rebalancing AVL Trees relies on "rotating" the tree's nodes
    #If a node is right heavy, perform a left rotation around the right subtree of the node.
    #If a node is left heavy, perform a right rotation around the left subtree of the node.
    
    #Left Rotation process:
    #Promote right child to root of tree
    #Move old root to be left child of new root
    #If new root already had a left child then make it right child of new left child. 
           
    #Similarly, rotating right is just the inverse. 
    #Right Rotation process: 
    #Promote left child to root of tree
    #Move old root to be right child of new root
    #If new root already had a right child then make it the left child of the new right child.
    
    #HOWEVER
    #If a subtree needs a left rotation to bring it into balance, first check the balance factor of the right child. If the right child is left heavy then do a right rotation on the right child, followed by the original left rotation. 
    #If a subtree needs a right rotation to bring it into balance, first check the balance factor fo the left child. If the left child is right heavy then do a left rotation on the left child, followed by the original rotation.
    
    #Proper rebalancing
    def rebalance(self,node):
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node) 
                
    def get(self,key):
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
    
    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)
    
    def __getitem__(self,key):
        return self.get(key)    

    def __contains__(self,key):
        if self._get(key,self.root):
            return True
        else:
            return False
        
    def delete(self,key):
        if self.size > 1:
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size-1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')
    
    def __delitem__(self,key):
        self.delete(key)    
    
class TreeNode:
    def __init__(self,key,val,left=None,right=None,
                                        parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
            
    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ
    
    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current
    
    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent   
                
    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChiLd:
                    yield elem
        yield self.key
        if self.hasRightChild():
            for elem in self.rightChild:
                yield elem    
    
mytree = BinarySearchTree()
mytree[3]="red"
mytree[4]="blue"
mytree[6]="yellow"
mytree[2]="at"

print(mytree[6])
print(mytree[2])