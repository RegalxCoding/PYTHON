class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def addNode(self,data):
        newNode=Node(data)
        
        if(self.head==None):
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode

    #display
    def display(self):
        current=self.head
        if(self.head==None):
            print("Linked List is empty")
            return
        print("Nodes of linked list are:")
        while(current!=None):
            print(current.data,end="\n",)
            current=current.next
    
    #adding node to end of the list
    def addToLast(self,data):
        newNode=Node(data)
        temp=self.tail
        self.tail.next=newNode
        self.tail=newNode

    #inserting node at the first
    def addToFirst(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode

    #deleting first node
    def delAtFirst(self):
        if self.head==None:
            print("lsit is empty")
        else:
            self.head=self.head.next
            if self.head==None:
                self.tail=None
    
    #deleting last node
    def delAtLast(self):
        current=self.head
        if(self.head==None):
            print("list is empty")
            return
        while(current.next and current.next.next):
            current=current.next
        current.next=None
        

    # def addToMid(self,data):
    #     newNode=Node(data)
    #     current=self.head
    #     cnt=0
    #     while(current!=None):
    #         cnt+=1
    #         current=current.next
    #     temp=self.head
    #     for i in range(int((cnt/2)-1)):
    #         print(temp.data)
    #         temp=temp.next
        
    #     nxt=temp.next.next
    #     temp.next=newNode
    #     temp=temp.next
    #     temp.next=nxt

slist=singlyLinkedList()
slist.addNode(2)
slist.addNode(4)
slist.addNode(6)
# slist.addToMid(9)
slist.addToLast(35)
slist.addToFirst(198)

# slist.delAtFirst()
# slist.delAtFirst()
# slist.delAtFirst()
# slist.delAtFirst()
# slist.delAtLast()
# slist.delAtLast()
slist.addToLast(999)
slist.addToFirst(101)

slist.display()
