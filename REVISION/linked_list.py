class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SinglyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def addNode(self,data):
        newNode=Node(data)

        if self.head==None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
        
    def display(self):
        current=self.head
        if self.head==None:
            print("list is empty")
            return
        print("nodes of linked list are:")
        while current!=None:
            print(current.data,end="->")
            current=current.next
        print("None")

    #add node to first
    def addToFirst(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
        if self.tail==None:
            self.tail=newNode

    #add node to last
    def addToLast(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
    
    #delete first node
    def delAtFirst(self):
        if self.head==None:
            print("list is empty, Nothing to delete")
        else:
            self.head=self.head.next
            if self.head==None:
                self.tail=None
    
    #delete last node
    def delAtLast(self):
        if self.head==None:
            print("lsit is empty, nothing to delete")
        elif self.head.next==None: #for only 1 node
             self.head=None
             self.tail=None
        else:                   #for multiple nodes
            current=self.head
            while current.next and current.next.next:
                current=current.next
            current.next=None

#user Interaction
l1=SinglyLinkedList()

while True:
    print("\nOption:\n1.Add Node to Start\n2.Add Node to End\n"
          "3.Delete First Node\n4.Delete Last Node\n5.Display\n6.Exit\n")
    ch=int(input("enter your choice:"))

    if ch==1:
        data=int(input("enter data to add at start:"))
        l1.addToFirst(data)
    elif ch==2:
        data=int(input("enter data to at end:"))
        l1.addToLast(data)
    elif ch==3:
        l1.delAtFirst()
    elif ch==4:
        l1.delAtLast()
    elif ch==5:
        l1.display()
    elif ch==6:
        print("exiting")
        break
    else:
        print("invalid choice:")

