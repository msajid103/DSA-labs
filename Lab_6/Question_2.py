class Stack:
    def __init__(self,parenthesis) :
        self.parenthesis = parenthesis
        self.next = None
class Linked_list:
    def __init__(self):
        self.head = None    
    def push(self,new):
        new.next = self.head
        self.head = new        
    def pop(self):
        self.head = self.head.next
    def peek(self):
        return self.head.parenthesis
    def isEmpty(self):
        if self.head == None:
            return True
        return False
    def expressionCheck(self,expre):    
        for i in range(len(expre)):
            if expre[i] == '[' or expre[i] == '{' or expre[i] == '(':
                self.push(Stack(expre[i])) 
            elif expre[i] == ']' and self.peek() == '[':
                self.pop()               
            elif expre[i] == '}' and self.peek() == '{':
                self.pop()               
            elif expre[i] == ')' and self.peek() == '(':
                self.pop()               
            else:
                print('Invalid Expression')
                return
        if self.isEmpty():
            print('Valid Expression')
        else:
            print('Invalid Expression')



lst = Linked_list()
expre = input('Enter  Parenthesis')
lst.expressionCheck(expre)
