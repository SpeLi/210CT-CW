def delnodes(self,value):
    if sel.node is None:
        return False
    elif self.root.value==data:
        if self.root.leftChild is None and self.root.rightCHild is  None: 
            self.root=None
        elif self.root.leftChild and self.root.rightChild is None:
            self.root= self.root.leftChild
        elif self.root.leftChild is None and self.root.rightChild:
            self.root= self.root.rightChild
        elif self.root.leftChild and self.root.rightChild:
            delNodeParent =delNode
            delNode= delnode.leftChild
            while delNode.leftChild:
                delNodeParent= delNode
                delNode=delNode.leftChild

            self.root.value = delNode.value
            if delNode.rightChild:
                if delNodeParent.value>delNode.value:




    parent =None
    node= self.root

    while node and node.value !=data
        
