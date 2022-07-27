class Node:
    __slots__='element','next'

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
        if(self.isempty()):
            self.head=newest
        else:
            self.tail.next=newest
            
        self.tail=newest
        self.size +=1
        
    def display(self):

         p=self.head
         while p:
             print(p.element,end='--->')
             p=p.next
         print()
L=LinkedList()
L.addlast(7)
L.addlast(4)
L.addlast(12)
L.addlast(8)
L.addlast(3)
L.display()
print('Size is',len(L))
