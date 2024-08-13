class Stack:
    def __init__(self,number) :
        self.number = number
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None    
    def push(self,new):
        new.next = self.head
        self.head = new 
    def printAll(self):
        head = self.head
        while head != None:
            print(head.number,end="")
            head = head.next
    def BinaryNumber(self,n):
        quotiont = n
        while quotiont > 1:
            self.push(Stack(quotiont % 2))
            quotiont = quotiont//2
        self.push(Stack(quotiont))
        
lst = Linked_list()
lst.BinaryNumber(25)
lst.printAll()
