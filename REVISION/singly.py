class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singly:
    def __init__(self):
        self.head=None

    def addtostart(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode
        
    def addtoend(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=newNode

    def addspecific(self,data,pos):
        newNode=Node(data)
        if pos==0:
            newNode.next=self.head
            self.head=newNode
        else:
            current=self.head
            for _ in range(pos-1):
                if not current:
                    print("pos out of bound")
                    return
                current=current.next
            newNode.next=current.next
            current.next=newNode
    
    def delfirst(self):
        if self.head is None:
            print("list is already empty")
        else:
            self.head=self.head.next
    
    def dellast(self):
        if self.head is None:
            print("list is already empty")
        elif self.head.next is None:
            self.head=None
        else:
            current=self.head
            while current.next.next:
                current=current.next
            current.next=None
    
    def delspecific(self,pos):
        if pos == 0:
            self.head=self.head.next
            return
        else:
            current=self.head
            for _ in range(pos-1):
                if not current or current.next:
                    print("pos out of bound")
                current=current.next
            current.next=current.next.next

    def search(self,value):
        if self.head is None:
            print("list is empyt")
            return
        current=self.head
        pos=0
        while current:
            if current.data==value:
                print(f"value {value} found at pos {pos}")
                return
            current=current.next
            pos+=1
        print("value not found")
                


    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            current=self.head
            print("Nodes in the linked list are:")
            while current:
                print(current.data,end=" ->")
                current=current.next
            print(None)
    
    

    
s=singly()
while True:
    print("\nMenu:")
    print("1. Insert at Start")
    print("2. Insert at End")
    print("3. Insert at Specific Position")
    print("4. Delete at Start")
    print("5. Delete at End")
    print("6. Delete at Specific Position")
    print("7. Traverse the List")
    print("8. search")
    print("9. Exit")

    ch=int(input("enter your choice:"))
    if ch==1:
        data=int(input("enter data to insert at first:"))
        s.addtostart(data)
    elif ch==2:
        data=int(input("enter data to insert at first:"))
        s.addtoend(data)
    elif ch==3:
        data=int(input("enter data to insert at specific pos:"))
        pos=int(input("enter pos:"))
        s.addspecific(data,pos)
    elif ch==4:
       s.delfirst()
    elif ch==5:
       s.dellast()
    elif ch==6:
        pos=int(input("enter pos:"))
        s.delspecific(pos)
    elif ch==7:
        s.display()
    elif ch==8:
        val=int(input("enter value to search:"))
        s.search(val)
    