class Stack:
    def __init__(self,number) :
        self.number = number
        self.next = None

class Linked_list:
    size = 0
    def __init__(self):
        self.head = None    
    def push(self,new):
        new.next = self.head
        self.head = new
        Linked_list.size += 1
    def pop(self):
        self.head = self.head.next
    def peek(self):
        print('Peek Number is ',self.head.number)
    def isEmpty(self):
        if self.head == None:
            return True
        return False
    def sizeStack(self):
        print('Size of Stack = ',Linked_list.size)   
    def revers(self):
        head = lst.head
        while head != None:
            self.push(Stack(head.number))
            head = head.next
    def printAll(self):
        head = self.head
        while head != None:
            print(head.number,end=' ')
            head = head.next
lst = Linked_list()
lst2 = Linked_list()
lst.push(Stack(1))
lst.push(Stack(2))
lst.push(Stack(3))
lst.push(Stack(4))
lst.printAll()
lst2.revers()
print('\nReverse List')
lst2.printAll()
