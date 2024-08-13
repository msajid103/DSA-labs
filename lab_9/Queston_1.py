class Node:
    def __init__(self,data):
        self.data = data
class Btree:
    def __init__(self):
        self.list = []
    def insert(self,data):
        self.list.append(Node(data))
    def left(self,value):
        for i in range(len(self.list)):
            if self.list[i].data == value and 2*i+1 < len(self.list):
                print(self.list[2*i+1].data)
                return
        print('Wrong Input')
           
    def right(self,value):
        for i in range(len(self.list)):
            if self.list[i].data == value and 2*i+2 < len(self.list):
                print(self.list[2*i+2].data)
                return
        print('Wrong Input')
    def Breath_First(self):
        for i in range(len(self.list)):        
            print(self.list[i].data)

            

b = Btree()

b.insert(1)
b.insert(2)
b.insert(3)
b.left(3)        
b.right(1) 
b.Breath_First()       