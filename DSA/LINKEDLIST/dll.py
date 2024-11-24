class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class dll:
    def __init__(self):
        self.head=None

    def addNode(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
        else:
            tail=self.head
            while(tail.next!=None):
                tail=tail.next
            tail.next=newNode
            newNode.prev=tail
        
    def display(self):
        if self.head==None:
            print("doubly linked list is empty!!")
            return
        print("Nodes of d linked list are:")
        temp=self.head
        while temp!=None:
            print(temp.data,end="->")
            temp=temp.next
        print(None)
    
    def insert_first(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
        else:
            self.head.prev=newNode
            newNode.next=self.head
            self.head=newNode
    def insert_last(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode
            newNode.prev=temp

    def del_first(self):
        if self.head==None:
            print("list is empty nothing to delete")
        else:
            self.head=self.head.next
            print("\nNode is deleted successfully....")

    def del_last(self):
        if self.head==None:
            print("list is empty nothing to delete")
        elif self.head.next==None:
            self.head=None
        else:
            temp=self.head
            while temp.next and temp.next.next:
                temp=temp.next
            temp.next=None
            print("\nnode deleted successfully...\n")
            

d1=dll()
while True:
    print("\nOPTION:\n1.Insert At Start\n2.Insert At End\n3.Display\n4.exit\n5.delete first node\n6.delete last node")
    choice=int(input("enter your choice:"))

    if choice==1:
        data=int(input("enter element to insert at first:"))
        d1.insert_first(data)
    elif choice==2:
         data=int(input("enter element to insert at last:"))
         d1.insert_last(data)
    elif choice==3:
        d1.display()
    elif choice==4:
        print("exiting....")
        break
    elif choice==5:
        d1.del_first()
    elif choice==6:
        d1.del_last()
    else:
        print("invalid choice please enter valid choice")

