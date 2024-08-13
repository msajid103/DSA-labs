class Person:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city
        self.next = None 
class linked_list:
    def __init__(self):
        self.start = None          
    def addAtStart(self,new):
        new.next = self.start
        self.start = new
    def removeFromEnd(self):
        start = self.start
        while start.next.next != None:          
            start = start.next
        start.next = None
    def AddAtEnd(self,new):
        start = self.start 
        if start == None:
            self.addAtStart(new)
            return       
        while start.next != None:          
            start = start.next       
        start.next = new
    def printAll(self):
        start = self.start
        while start != None:
            print (start.age)
            start = start.next

        
lst = linked_list()
lst.addAtStart(Person('Faizai',18,'mainwali'))
lst.addAtStart(Person('Faizai',19,'mainwali'))
lst.addAtStart(Person('Faizai',20,'mainwali'))
lst.addAtStart(Person('Faizai',21,'mainwali'))
lst.removeFromEnd()
lst.AddAtEnd(Person('ali',100,'mainwali'))
lst.printAll()
