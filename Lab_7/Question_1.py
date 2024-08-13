class Job:
    def __init__(self,title,id,purpose):
        self.title = title
        self.id = id 
        self.purpose = purpose
        self.next = None
class Linked_list:
    def __init__(self) :
        self.head = None
        self.tail = None
    def enqueue(self,new):
        if self.head == None:
            new.next = self.head
            self.head = new
            self.tail = new
            print('Item Enqueue')
        else:   
            self.tail.next = new
            self.tail = new
            print('Item Enqueued')
    def dequeue(self):
        if self.head == None:
            print('List is already Empty')
        else:    
            self.head = self.head.next
            print('Item Dequeued')
    def isEmpty(self):
        if self.head == None:
            print('List is Empty')
        else:
            print("List is not Empty")
    def size(self):
        head = self.head
        size = 0
        while head != None:
            size += 1
            head = head.next
        print('Size of List = ',size)   
    def display(self):
        head = self.head       
        while head != None:
            print('Title is ',head.title,' id is ',head.id,' Purpose is ',head.purpose)
            head = head.next
    def search(self,name):
        head = self.head       
        while head != None:
            if head.title == name:
                print(name,",Yes exist")
                return
            head = head.next
        print(name,' Does not Exist')

   
    


lst = Linked_list()
lst.enqueue(Job('PAF',123,"defence"))
lst.enqueue(Job('Navy',1,"water defence"))
lst.enqueue(Job('Army',2,"Border defence"))
lst.isEmpty()
lst.size()
lst.display()
lst.search('PAF')

        