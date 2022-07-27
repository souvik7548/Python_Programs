class Node:
    __Slots__='element','next'

    def __init__(self,element,next):
        self.element=element
        self.next=next
class CircularLinkedList:

    def __init__(self):
        self.head=None
        self.tail=None
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
        
    def display(self):
        p=self.head
        i=0
        while i<len(self):
            print(p.element,end=' ===>')
            p=p.next
            i+=1
        print()
        
    def search(self,key):
        p=self.head
        index=0
        while index<len(self):
            if p.element==key:
                return index

            p=p.next
            index+=1
        return -1
C = CircularLinkedList()
C.addlast(7)
C.addlast(4)
C.addlast(12)
C.display()
print('Size:',len(C))
C.addlast(8)
C.addlast(3)
C.display()
print('Size:',len(C))

    
