class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0

    def enqueue(self,data):
        newNode=Node(data)
        if self.rear is None:
            self.front=self.rear=newNode
        else:
            self.rear.next=newNode
            self.rear=newNode
        self.size+=1
        print(f"{data} data inserted in queue successfully")

    def dequeue(self):
        if self.is_empty():
            print("queue is already empty")
            return None
        deq_data=self.front.data
        self.front=self.front.next
        if self.front is None:
            self.rear= None
        self.size-=1
        print(f"{deq_data} is dequeued")

    def peek(self):
        if self.is_empty():
            print("list is already empty")
            return None
        print(f"top of queue:{self.front.data}")

    def display(self):
        if self.is_empty():
            print("queue is empty")
            return
        current=self.front
        print("queue elements:")
        while current:
            print(current.data,end="->")
            current=current.next
        print("None")



    def is_empty(self):
        return self.front is None

q=Queue()
while True:
    print("Options\n1.push\n2.pop\n3.peek\n4.traverse")
    choice=int(input("enter your choice:"))

    if choice==1:
        data=int(input("enter data to insert in queue:"))
        q.enqueue(data)
    elif choice==2:
        q.dequeue()
    elif choice==3:
        q.peek()
    elif choice==4:
        q.display()
    else:
        print("invalid choice")
    