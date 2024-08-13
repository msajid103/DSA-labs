class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class Btree:
    def __init__(self):
        self.root = None
    def insert(self,data):
        if self.root == None:
            self.root = Node(data)           
            return
        root = [self.root]        
        while root[0] != None:
            if root[0].left == None:              
                root[0].left = Node(data)
                break
            elif root[0].right == None:  
                root[0].right = Node(data)
                break
            root.extend([root[0].left,root[0].right])
            root.pop(0)     
    def Breath_First(self):
        root = [self.root]        
        while root[0] != None:
            print (root[0].data)
            root.extend([root[0].left,root[0].right])
            root.pop(0)
    
b = Btree()
b.insert(1)
b.insert(2)
b.insert(3)
b.insert(4)
b.insert(5)
b.Breath_First()