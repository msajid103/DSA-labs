class Student:
    def __init__(self,name,roll_no,cgpa,department):
        self.name = name
        self.roll_no = roll_no
        self.cgpa = cgpa
        self.department = department
class Queue:
    def __init__(self,max_size):
        self.max_size = max_size
        self.lst = []
        for i in range(self.max_size):
            self.lst.append('None')
        self.head = 0
        self.tail = 0
        self.size = 0

    def enqueue(self,new):
        if self.size < self.max_size-1:
            self.lst[self.tail] = new
            self.tail = (self.tail+1) % self.max_size
            self.size += 1
            print('Item Enqueued')
        else:
            print('List Full')
    def dequeu(self):
        if self.size != 0:
            self.head = (self.head+1) % self.max_size
            print('Item Dequeued')
            self.size -= 1
        else:
            print('List is already Empty')
    def isEmpty(self):
        if self.size == 0:
            print('List is Empty')
        else:
            print('List id not Empty')
    def size(self):
        print('Size of List =',self.size)
    def display(self):
        head = self.head    
        while head != self.tail:
            print(self.lst[head].name)
            head = (head+1) % self.max_size
    def search(self,name):
        head = self.head    
        while head != self.tail:
            if self.lst[head].name == name:
                print(name,'Exist in list')
                return            
            head = (head+1) % self.max_size
        print(name,"does't Exist")
         





lst = Queue(4)
lst.enqueue(Student('sajid',1,3.4,'BBA'))
lst.enqueue(Student('ali',2,3.2,'CS'))
lst.enqueue(Student('sadaqat',3,3.3,'EE'))
lst.dequeu()
lst.display()
lst.search('ali')
