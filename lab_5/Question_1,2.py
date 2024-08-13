class Subject:
    def __init__(self,title,cre_h,semester,instructer):
        self.title = title
        self.cre_h = cre_h
        self.semester = semester
        self.instructer = instructer
        self.next = None
        self.back = None
class Linked_list:
    count = 0
    def __init__(self):
        self.start = None      
    def AddAtStart(self,new):
        new.next = self.start        
        self.start = new
        if self.start.next != None:
            self.start.next.back = self.start          
        Linked_list.count += 1
        print('Added at Start')
    def removeFromStart(self):
        if self.start == None:
            print('List already Empty')
        else:
            self.start = self.start.next
            if self.start != None:
                self.start.back = None
            print('Remove from Start')
            Linked_list.count -= 1
    def AddAtEnd(self,new):
            start = self.start 
            if start == None:
                self.AddAtStart(new)
                return       
            while start.next != None:          
                start = start.next
            new.back = start       
            start.next = new
            Linked_list.count += 1
            print('Added at End')
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
    def searchByTitle(self,title):
        start = self.start
        while start != None:
            if start.title == title:
                return True
            start = start.next
        return False
    def AddBeforePosition(self,new,position):
        if position > Linked_list.count:
            print("Enter approperiat position to add !")
            return
        if position == 0:
            self.AddAtStart(new)
            return 
        i = 1  
        start = self.start 
        while i < position:                         
            start = start.next  
            i += 1   
        new.next = start.next
        start.next.back = new
        start.next = new
        new.back = start
        print('Added before That Position') 
        Linked_list.count += 1
    def removeBeforePosition(self,position):
            if position > Linked_list.count-1:
                print("Enter approperiat position to remove !")
                return
            if position == 0:
                self.removeFromStart()
                return 
            i = 1  
            start = self.start 
            while i < position:                      
                start = start.next  
                i += 1 
            start.next = start.next.next 
            if start.next != None:
                start.next.back = start
            print('Removed Before That Position') 
            Linked_list.count -= 1
    def Display_Befor_After_Position(self,position):
            if position > Linked_list.count-2 or position < 1:
                print("Enter approperiat position to print value")
                return
            start = self.start            
            i = 0      
            while start != None: 
                if i == position:
                    print (f"Subject = {start.next.title} | Credit Hour = {start.next.cre_h} | Instructer = {start.next.instructer} | Semester = {start.next.semester}")
                    print (f"Subject = {start.back.title} | Credit Hour = {start.back.cre_h} | Instructer = {start.back.instructer} | Semester = {start.back.semester}")
                start = start.next  
                i += 1    
    def printSubjects(self):          
        start = self.start 
        back = None             
        while start != None:           
            print('_____________________________________________')
            print (f"Subject = {start.title} | Credit Hour = {start.cre_h} | Instructer = {start.instructer} | Semester = {start.semester}")
            back = start
            start = start.next  
        print('Back print')         
        while back != None: 
            print('_____________________________________________')
            print (f"Subject = {back.title} | Credit Hour = {back.cre_h} | Instructer = {back.instructer} | Semester = {back.semester}")
            back = back.back   
    def size(self):
        print(f'Total subjects = {Linked_list.count}') 
    def ExitProgramme(self):
        print('Programe Exited')
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
            self.AddBeforePosition(Subject(title,cr_h,semester,instructer),position)
            self.functionalty()
        elif key == 'f':
            position = int(input('Enter position to remove :'))
            self.removeBeforePosition(position)
            self.functionalty()
        elif key == 'g':
            position = int(input('Enter position to Display :'))
            self.Display_Befor_After_Position(position) 
            self.functionalty()
        elif key == 'h':
            title = input('Enter title of subject to search :')
            print(self.searchByTitle(title))
            self.functionalty()
        elif key == 'i':
            self.size()
            self.functionalty()
        elif key == 'j':
            self.printSubjects()
            self.functionalty()
        elif key == 'k':
            self.ExitProgramme()
        else:
            print('Enter correct Value')
            self.functionalty()  
                
        
     
lst = Linked_list()
key = ['a','b','c','d','e','f','g','h','i','j','k']
value= ['addAtStart','RemoveFromStart','addAtEnd','RemoveFromEnd','addBeforePosition','RemoveBeforePosition','Display_before_after_Position','SearchSubject','SizeOfSubject','DisplayAllSubject','Exit']
for i in range(len(key)):
    print(f'Enter {key[i]} for {value[i]}')
lst.functionalty()