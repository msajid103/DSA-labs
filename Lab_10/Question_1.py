
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
class AVLtree:
    count = 0
    def insert(self,data,root):        
        if root is None:
            # AVLtree.count += 1
            return Node(data)
        elif data > root.data:
            root.right = self.insert(data,root.right)
        else:
            root.left = self.insert(data, root.left)
        root.height = 1+ max(self.getHeight(root.left), self.getHeight(root.right))
        bf = self.getHeight(root.left)-self.getHeight(root.right)
        if bf < -1 and data > root.right.data:
            return self.leftRotation(root)
        if bf < -1 and data < root.right.data:
            root.right = self.rightRotation(root.right)
            return  self.leftRotation(root)
        if bf > 1 and data < root.left.data:
            print('went')
            return self.rightRotation(root)
        if bf > 1 and data > root.left.data:
            root.left = self.leftRotation(root.left)
            return self.rightRotation(root)        
        return root
    def getHeight(self, root):
        if not root:
            return 0
        return root.height
        # return 1 + max(self.getHeight(root.left),self.getHeight(root.right))
    def leftRotation(self,root):
        # AVLtree.count += 1
        y = root.right
        t = y.left
        y.left = root
        root.right = t
        root.height = 1+ max(self.getHeight(root.left), self.getHeight(root.right))
        return y
    def rightRotation(self,root):
        # AVLtree.count += 1
        y = root.left
        t = y.right
        y.right = root
        root.left = t
        root.height = 1+ max(self.getHeight(root.left), self.getHeight(root.right))
        return y  
    def preorder(self, root):
        if root == None:
            return
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)  
    def inorder(self,root):
        if root==None:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right) 

t = AVLtree()
root = None
root = t.insert(40,root)
root = t.insert(20,root)
root = t.insert(43,root)
root = t.insert(230,root)
root = t.insert(2,root)
root = t.insert(1,root)
print('Inorder')
t.preorder(root)
# t.inorder(root)
# print(root.left.right.data,root.left.right.height)


