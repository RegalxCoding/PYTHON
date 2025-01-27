class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.top=None
    
    def push(self,data):
        newNode=Node(data)
        newNode.next=self.top
        self.top=newNode
        print(f"{data} push in stack")

    def pop(self):
        if self.is_empty():
            print("list is already empty nothing to pop")
            return
        pop_data=self.top.data
        self.top=self.top.next
        print(f"{pop_data} popped successfully")
    
    def peek(self):
        if self.is_empty():
            print("stack is empty")
            return None
        print(f"Top of Stack: {self.top.data}")
        

    def traverse(self):
        if self.is_empty():
            print("stack is empty")
            return
        current=self.top
        while current:
            print(current.data)
            current=current.next


    def is_empty(self):
        return self.top is None

s=stack()
while True:
    print("Options\n1.push\n2.pop\n3.peek\n4.traverse")
    choice=int(input("enter your choice:"))

    if choice==1:
        data=int(input("enter data to push in stack:"))
        s.push(data)
    elif choice==2:
        s.pop()
    elif choice==3:
        s.peek()
    elif choice==4:
        s.traverse()
    else:
        print("invalid choice")