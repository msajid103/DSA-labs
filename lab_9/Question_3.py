
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class BinarySearchtree:
    def __init__(self):
        self.root = None
    def insert(self,data,root):
        if self.root == None:
            self.root = node(data)
        else:          
            if data <= root.data:
                if root.left == None:
                    root.left = node(data)
                    return
                self.insert(data,root.left)
            elif data > root.data:
                if root.right == None:
                    root.right = node(data)
                    return
                self.insert(data,root.right)
        

    def preorder(self, root):
        if root==None:
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
       
tree = BinarySearchtree()
tree.insert(100,tree.root)
tree.insert(300,tree.root)
tree.insert(20,tree.root)
tree.insert(3100,tree.root)
tree.insert(2100,tree.root)
tree.insert(2,tree.root)
print('---------PreOrder----------')
tree.preorder(tree.root)


print('---------InOrder----------')
tree.inorder(tree.root)
 


