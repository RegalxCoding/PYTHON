class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None   #initialize of empty stack
    
    def is_empty(self):
        if self.top==None:
            print("Top is empty")

    def push(self,data):
        newNode=Node(data)
        newNode.next=self.top
        self.top=newNode

    def pop(self):
        if self.is_empty():
            return
        pop_data=self.top.data
        self.top=self.top.next
        print("popped data:",pop_data)