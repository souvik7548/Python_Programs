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
        
    def removeany(self, position):
        p = self.head
        i = 1
        while i < position - 1:
            p = p.next
            i = i + 1
        e = p.next.element
        p.next = p.next.next
        self.size -= 1
        return e      
    
C = CircularLinkedList()
C.addlast(7)
C.addlast(4)
C.addlast(12)
C.addlast(8)
C.addlast(3)

print('Size:',len(C))
ele=C.removeany(5)
print(" Element {} removed  :".format(ele))








    
        
