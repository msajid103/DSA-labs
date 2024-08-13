class Stack:
    def __init__(self,data) :
        self.data = data
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
        return self.head.data
    def isEmpty(self):
        if self.head == None:
            return True
        return False
    def sizeStack(self):
        print('Size of Stack = ',Linked_list.size)   
    def revers(self):
        head = lst.head
        while head != None:
            self.push(Stack(head.data))
            head = head.next
    def printAll(self):
        head = self.head
        while head != None:
            print(head.data,end=' ')
            head = head.next
    def addstring(self,str):
        for i in str:
            lst.push(Stack(i))
def checkpalandrom(lst,lst2):
    # print(self.peek())
    # while self.isEmpty():
    #     if self.peek() == lst2.peek():
    #         self.pop()
    #         lst2.pop()
    print(lst.peek(),lst2.peek())
    if lst.head == None:
        return True
    if lst.peek() == lst2.peek():
        lst.pop()
        lst2.pop()
        checkpalandrom(lst,lst2)
    else:
        return False


lst = Linked_list()
lst2 = Linked_list()
str = input('Enter string : ')
lst.addstring(str)
lst2.revers()
print(checkpalandrom(lst,lst2))
print(lst.peek())

