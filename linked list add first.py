class Node:
    __Slots__='element','next'

    def __init__(self,element,next):
        self.element=element
        self.next=next
        
class LinkedList:
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
            self.head=newest
        else:
            self.tail.next=newest
        self.tail=newest
        self.size+=1

    def display(self):
        p=self.head
        while p:
            print(p.element,end='===>')
            p=p.next
        print()

    def search(self,key):
        p = self._head
        index = 0
        while p:
            if p._element == key:
                return index
            p = p._next
            index = index + 1
        return -1

    def addfirst(self,e):
        newest=Node(e,None)
        if self.isempty():
            self.head=newest
            self.tail=newest
        else:
            newest.next=self.head
            self.head=newest
        self.size+=1
L = LinkedList()
L.addlast(7)
L.addlast(4)
L.addlast(12)
L.addlast(8)
L.addlast(3)
L.display()
print('Size:',len(L))
L.addfirst(15)
L.display()
print('Size:',len(L))
L.addfirst(25)
L.display()
print('Size:',len(L))
L.addlast(35)
L.display()
print('Size:',len(L))


        
        
