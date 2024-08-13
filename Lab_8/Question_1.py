class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Btree:
    def __init__(self):
        self.root = None
# write code to implement below traversal funcitons
    def in_order(self,root):
        if root == None:
            return  
        else:
            self.in_order(root.left)
            print(root.data)
            self.in_order(root.right)
    def depth_first(self,root):
        if root == None:
            return  
        else:
            self.depth_first(root.left)
            self.depth_first(root.right)
            print(root.data)  
tree = Btree()
tree.root = node(20)
tree.root.left = node(10)
tree.root.right = node(30)
tree.root.left.left = node(100)
tree.root.left.right = node(45)
tree.root.right.left = node(50)
tree.root.right.right = node(90)
tree.root.left.left.left = node(110)
tree.root.left.left.right = node(230)
tree.root.left.right.left = node(105)
tree.root.left.right.right = node(188)
tree.root.right.left.left = node(122)
tree.root.right.left.right = node(43)
tree.root.right.right.left = node (55)
tree.root.right.right.right = node (360)

print('__________IN Oder traversal___________')
tree.in_order(tree.root)

print('__________ Depth First traversal___________')
tree.depth_first(tree.root)