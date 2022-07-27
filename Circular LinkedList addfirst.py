class Node:
    __slots__='element','next'
    def __init__(self,element,next):
        self.element=element
        self.next=next
        
class CircularLinkedList:
    
    def __init__(self):
        self.head=None
        self.none=None
        self.size=0
        
    def __len__(self):
        return self.size
    
    def isempty(self):
        return self.size==0

    def addlast(self,e):
        newest=Node(e,None)
        if self.isempty():
            newest.next=newest
            self.head=newest
        else:
            newest.next=self.tail.next
            self.tail.next=newest
        self.tail=newest
        self.size+=1
        
    def addfirst(self,e):
        newest=Node(e,None)
        if self.isempty():
            newest.next=newest
            self.head=newest
            self.tail=newest
        else:
            self.tail.next=newest
            newest.next=self.head
            self.head=newest
        self.size+=1
    def display(self):
        p=self.head
        i=0
        while i<len(self):
            print(p.element,end='===>')
            p=p.next
            i+=1
        print()
C=CircularLinkedList()
C.addlast(7)
C.addlast(4)
C.addlast(12)
C.addlast(8)
C.addlast(3)
C.display()
print('Size Of CLL',len(C))
print("After Adding Node At First Position")
C.addfirst(25)
C.display()
print("Size is ",len(C))

        
        
        
