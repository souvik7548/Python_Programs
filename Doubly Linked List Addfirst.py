class Node:
    __Slots__='elements','next','prev'

    def __init__(self,element,next,prev):
        self.element=element
        self.next=next
        self.prev=prev
        
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def __len__(self):
        return self.size
    
    def isempty(self):
        return self.size==0
    
    def addlast(self,e):
        newest=Node(e,None,None)
        if self.isempty():
            self.head=newest
            self.tail=newest
        else:
            self.tail.next=newest
            newest.prev=self.tail
            self.tail=newest
        self.size +=1
        
    def addfirst(self,e):
        newest=Node(e,None,None)
        if self.isempty():
            self.head=newest
            self.tail=newest
        else:
            newest.next=self.head
            self.head.previous=newest
            self.head=newest
        self.size+=1
        
    def addany(self,e,position):
        newest=Node(e,None,None)
        p=self.head
        i=1
        while i<position-1:
            p=p.next
            i+=1
        newest.next=p.next
        p.next.prev=newest
        p.next=newest
        newest.prev=p
        self.size+=1
    def display(self):
        p=self.head
        while p:
            print(p.element,end='-->')
            p=p.next
        print()
        
    def displayrev(self):
        p=self.tail
        while p:
            print(p.element,end='<---')
            p=p.prev
        print()
L=DoublyLinkedList()
L.addlast(7)
L.addlast(4)
L.addlast(12)
L.addlast(8)
L.addlast(3)
L.addfirst(70)
L.addany(3,25)
print("Display The  Doubly-Linked List")
L.display()
print("Displayed The  Doubly-Linked List In Previos Order")
L.displayrev()
print("The Length Of The Doubly-Linked List is",len(L))

