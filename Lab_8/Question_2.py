class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.middle = None
class Tree:
    def __init__(self):
        self.root = None
    #write code to implement below traversal funcitons
    def Breath_First(self):
        root = [self.root]        
        while len(root) != 0:
            if root[0] != None:
                print (root[0].data)
                root.extend([root[0].left,root[0].middle,root[0].right])
            root.pop(0)   
tree = Tree()
tree.root = node (20)
tree.root.left = node (10)
tree.root.middle = node (1220)
tree.root.middle.left = node (2220)
tree.root.middle.middle = node (3220)
tree.root.right = node (30)
tree.root.left.left = node (100)
tree.root.left.right = node (45)
tree.root.right.left = node (50)
tree.root.right.right = node (90)
tree.root.left.left.left = node (110)
tree.root.left.left.right = node (230)
tree.root.left.right.left = node (105)
tree.root.left.right.right = node (188)
tree.root.right.left.left = node (122)
tree.root.right.left.right = node (43)
tree.root.right.right.left = node (55)
tree.root.right.right.right = node (360)
#write code to call traversal function and then call main function.
tree.Breath_First()