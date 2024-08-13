class Book:
    def __init__(self,title,author,edition):
        self.title = title
        self.author = author
        self.edition = edition
        self.next = None
class Linked_list:
    count = 0
    def __init__(self):
        self.start = None
    def AddAtStart(self,new):
        new.next = self.start
        self.start = new
        Linked_list.count += 1
        print('Added at start')
    def AddAtEnd(self,new):
            start = self.start 
            if start == None:
                self.AddAtStart(new)
                return       
            while start.next != None:          
                start = start.next       
            start.next = new
            Linked_list.count += 1
            print('Added at End')
    def removeFromStart(self):
        if self.start == None:
            print('List already Empty')
        else:
            self.start = self.start.next
            Linked_list.count -= 1
            print('Removed From Start')
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
        print('Remove from End')
        Linked_list.count -= 1
    def printBook(self):      
        start = self.start      
        while start != None:
            print (f"This is '{start.title}' Book '{start.edition} edition' and Written by '{start.author}'")
            start = start.next
    def searchByTitle(self,title):
        start = self.start
        while start != None:
            if start.title == title:
                return True
            start = start.next
        return False
    def functionalty(self):
        print('------------------->')     
        key = input('Enter Value For Functionalty :') 
        if key == 'a':
            title = input('Enter Title of Book :')
            author = input('Enter Author Name :')
            edition = input('Enter Edition of Book :')
            self.AddAtStart(Book(title,author,edition))
            self.functionalty()
        elif key == 'b':
            title = input('Enter Title of Book :')
            author = input('Enter Author Name :')
            edition = input('Enter Edition of Book :')
            self.AddAtEnd(Book(title,author,edition))
            self.functionalty()
        elif key == 'c':
            self.removeFromStart()
            self.functionalty()
        elif key == 'd':
            self.removeFromEnd()
            self.functionalty()
        elif key == 'e':
            self.printBook()
            self.functionalty()
        elif key == 'f':
            title = input('Enter Title of Book :')
            print(self.searchByTitle(title))
            self.functionalty()
        elif key == 'g':
            print(self.count)
            self.functionalty()
        elif key == 'h':
            print('Programe Exit')
            return
        else:
            print('Enter correct Value')
            self.functionalty()        

# lst = Linked_list()
# key = ['a','b','c','d','e','f','g','h']
# value= ['addAtStart','addAtEnd','RemoveFromStart','RemoveFromEnd','DisplayAllBook','SearchBook','CountBook','Exit']
# for i in range(len(key)):
#     print(f'Enter {key[i]} for {value[i]}')
# lst.functionalty()

b1 = Book('a','sadaqat',6)
b2 = Book('b','sadaqat',5)

b1.next = b2
print(b1.next.title)