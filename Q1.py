# 220CT-CW
# BinarySearchTree()

# Building nodes in a binary search tree
class bstNode: 
    def _init_(self,value):
        self.value=value
        self.left=None
        self.right=None
        self.count =1
    # use a string representation of the object(nodes)
    def _str_(self): 
        return 'value:{0},count:{1}'.format(self.value,self.count)
    # insert nodes into binary search tree
def Insert(root,value):
    if not root:
        return bstNode(value)
    elif root.value == value:
            root.count +=1
    elif value< root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return(root)
    #find 
def search(root, word, depth=1):
    if not root:
        return(0,0)
    elif root.value ==word:
         return(depth,root,count)
    elif word < root.value:
        return(search(root.left,word,depth+1))
    else:
        return search(root.right, word, pepth+1

def print_tree(root):
    if root:
        print_tree(root.left)
        print (root) in src:
        print ('search {0}, result: {1}'.format(word, search(tree, word)))
  
    
