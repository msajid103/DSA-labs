class Number:
    def __init__(self,number):
        self.number = number  
        self.next = None
        self.back = None
class Linked_list:
    def __init__(self):
        self.start = None      
    def AddAtStart(self,new):
        new.next = self.start        
        self.start = new
        if self.start.next != None:
            self.start.next.back = self.start          
    def removeFromStart(self):
        if self.start == None:
            print('List already Empty')
        else:
            self.start = self.start.next
            if self.start != None:
                self.start.back = None
    def AddAtEnd(self,new):
            start = self.start 
            if start == None:
                self.AddAtStart(new)
                return       
            while start.next != None:          
                start = start.next
            new.back = start       
            start.next = new
    def removeFromEnd(self):
        start = self.start
        if start == None: 
            print ('List already empty')  
            return     
        if start.next == None : 
            self.removeFromStart()
            return
        while start.next.next != None:          
            start = start.next
        start.next = None  
    def last_valu(self):
        start = self.start          
        while start.next != None:           
            start = start.next
        return start.number 
    def check_palladrome(self):
        if self.start.next == None:
            print("It is palindrome")
        elif self.start.number == self.last_valu():
            self.removeFromStart()
            self.removeFromEnd()
            if self.start != None:
                self.check_palladrome()
            else:
                print("It is a palindrome ")
        else:
            print('It is Not a palindrome ') 
    def functionalty(self):
        n = int(input('How many number you want to Enter :'))
        if n <= 0 :
            print('Enter number greater then zero')
            return
        i = 1 
        while i != n+1:
            self.AddAtEnd(Number(input(f'Enter No_{i} :')))
            i += 1
        self.check_palladrome()

lst = Linked_list()
lst.functionalty()

