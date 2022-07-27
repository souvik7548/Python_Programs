class Node:
    __slots__='element','next'
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
        return self.size ==0

    def addlast(self, e):
        newest = Node(e, None)
        if self.isempty():
            newest.next = newest
            self.head = newest
        else:
            newest.next = self.tail.next
            self.tail.next = newest
        self.tail = newest
        self.size += 1
    def removefirst(self):
        if self.isempty():
            print('List Is Empty')
            return
        e=self.head.element
        self.tail.next=self.head.next
        self.head=self.head.next
        self.size-=1
        if self.isempty():
            self.head=None
            self.tail=None
        return e

C = CircularLinkedList()
C.addlast(7)
C.addlast(4)
C.addlast(12)
C.addlast(8)
C.addlast(3)

print('Size:',len(C))
ele=C.removefirst()
print("removed element is :",ele)
print('Size:',len(C))









    
        
