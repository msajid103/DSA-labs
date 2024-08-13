class Subject:
    def __init__(self,title,cre_h,semester,instructer):
        self.title = title
        self.cre_h = cre_h
        self.semester = semester
        self.instructer = instructer
        self.next = None
class Linked_list:
    count = 0
    def __init__(self):
        self.start = None
    def AddAtStart(self,new):
        print(new.title)
        # new.next = self.start
        # self.start = new
        # Linked_list.count += 1
        # print('Added at Start')
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
    def AddAtPosition(self,new,position):
            if position > Linked_list.count+1:
                print("Enter approperiat position to add !")
                return
            start = self.start 
            if position == 1:
                self.AddAtStart(new)
                return 
            i = 2      
            while start != None: 
                if i == position:
                    new.next = start.next
                    start.next = new   
                    print('Added at That Position')      
                start = start.next  
                i += 1    
            Linked_list.count += 1
    def DisplayAtPosition(self,position):
            if position > Linked_list.count+1 or position < 1:
                print("Enter approperiat position to print value")
                return
            start = self.start            
            i = 1      
            while start != None: 
                if i == position:
                    print (f"Subject = {start.title} | Credit Hour = {start.cre_h} | Instructer = {start.instructer} | Semester = {start.semester}")
                start = start.next  
                i += 1    
    def removeFromPosition(self,position):
            if position > Linked_list.count:
                print("Enter approperiat position to remove !")
                return
            start = self.start 
            if position == 1:
                self.removeFromStart()
                return 
            i = 2      
            while start != None: 
                if i == position:
                    start.next = start.next.next 
                    print('Removed From That Position') 
                    Linked_list.count -= 1
                start = start.next  
                i += 1    
    def removeFromStart(self):
        if self.start == None:
            print('List already Empty')
        else:
            self.start = self.start.next
            print('Remove from Start')
            Linked_list.count -= 1
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
    def printSubjects(self):      
        start = self.start      
        while start != None:
            print('_____________________________________________')
            print (f"Subject = {start.title} | Credit Hour = {start.cre_h} | Instructer = {start.instructer} | Semester = {start.semester}")
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
            title = input('Enter Title of Subject :')
            cr_h = input('Enter Credit Hour of Subject :')
            semester = input('Enter Semester :')
            instructer = input('Enter Instructer of Subject :')
            self.AddAtStart(Subject(title,cr_h,semester,instructer))
            self.functionalty()
        elif key == 'c':
            title = input('Enter Title of Subject :')
            cr_h = input('Enter Credit Hour of Subject :')
            semester = input('Enter Semester :')
            instructer = input('Enter Instructer of Subject :')
            self.AddAtEnd(Subject(title,cr_h,semester,instructer))
            self.functionalty()
        elif key == 'b':
            self.removeFromStart()
            self.functionalty()
        elif key == 'd':
            self.removeFromEnd()
            self.functionalty()
        elif key == 'e':
            title = input('Enter Title of Subject :')
            cr_h = input('Enter Credit Hour of Subject :')
            semester = input('Enter Semester :')
            instructer = input('Enter Instructer of Subject :')
            position = int(input('Enter the position to add :'))
            self.AddAtPosition(Subject(title,cr_h,semester,instructer),position)
            self.functionalty()
        elif key == 'f':
            position = int(input('Enter position to remove :'))
            self.removeFromPosition(position)
            self.functionalty()
        elif key == 'g':
            position = int(input('Enter position to Display :'))
            self.DisplayAtPosition(position) 
            self.functionalty()
        elif key == 'h':
            title = input('Enter title of subject to search :')
            print(self.searchByTitle(title))
            self.functionalty()
        elif key == 'i':
            print('Size of subjects =',self.count)
            self.functionalty()
        elif key == 'j':
            self.printSubjects()
            self.functionalty()
        elif key == 'k':
            print('Programe Exit')
            return
        else:
            print('Enter correct Value')
            self.functionalty()        

# lst = Linked_list()
# key = ['a','b','c','d','e','f','g','h','i','j','k']
# value= ['addAtStart','RemoveFromStart','addAtEnd','RemoveFromEnd','addatPosition','RemoveFromPosition','DisplayaAPosition','SearchSubject','SizeOfSubject','DisplayAllSubject','Exit']
# for i in range(len(key)):
#     print(f'Enter {key[i]} for {value[i]}')
# lst.functionalty()
l = Linked_list()
s1 = Subject(1,2,3,4)
# print(s1.next)
l.AddAtStart(s1)
# print(Subject.title)