class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class Doubly:
    def __init__(self):
        self.head=None
        self.temp=None
    def addNode(self,data):
        newNode=Node(data)

        if(self.head==None):
            self.head=newNode
            self.temp=newNode
        else:
           self.temp.next=newNode
           newNode.previous=self.temp
           newNode.next=None
           self.temp=self.temp.next
    def display(self):
        current=self.head
        if(current==None):
            print("list is empty")
        else:
            while(current!=None):
                print(current.data)
                current=current.next
d1=Doubly()
d1.addNode(2)
d1.addNode(4)
d1.addNode(5)
d1.addNode(8)
d1.display()


