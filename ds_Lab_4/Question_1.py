class Node:
    def __init__(self,number):
        self.number = number
        self.neibour = None 
class Main:
    def __init__(self):
        self.start = None          
    def addAtStart(self,x):
        x.neibour = self.start
        self.start = x
    def removeFromStart(self):
        self.start = self.start.neibour
    def printAll(self):
        start = self.start
        while start != None:
            print (start.number)
            start = start.neibour

        
my = Main()
my.addAtStart(Node(1))
my.addAtStart(Node(2))
my.addAtStart(Node(3))
my.removeFromStart()
my.printAll()


        