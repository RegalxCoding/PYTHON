# Algorithm to Sort a Singly Linked List (Using Bubble Sort)
# 1.Check if the List is Empty:

# If the head of the list is None or there is only one node (head.next == None), the list is already sorted.
# 2.Outer Loop for Passes:

# Use a while loop that continues until no swaps are needed in a pass (sorted flag becomes False).
# 3.Inner Loop for Comparisons:

# Start from the head of the list and traverse it.
# Compare the data of the current node with the next node.
# If the data of the current node is greater than the next node, swap the data values.
# 4.Repeat Until Sorted:

# Continue making passes until no swaps are needed, indicating the list is sorted.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode

    def sortList(self):
        if self.head is None or self.head.next is None:
            return  # List is already sorted if empty or has one node
        
        sorted_flag = False
        while not sorted_flag:
            sorted_flag = True
            current = self.head
            while current.next is not None:
                if current.data > current.next.data:
                    # Swap the data
                    current.data, current.next.data = current.next.data, current.data
                    sorted_flag = False
                current = current.next

    def display(self):
        if self.head is None:
            print("List is empty.")
        else:
            current = self.head
            print("Nodes in the linked list are:")
            while current is not None:
                print(current.data, end=" -> ")
                current = current.next
            print("None")

# Driver Code
sll = SinglyLinkedList()
while True:
    print("\nMenu:")
    print("1. Add Node")
    print("2. Sort List")
    print("3. Display List")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter data to add: "))
        sll.addNode(data)
    elif choice == 2:
        sll.sortList()
        print("List sorted successfully.")
    elif choice == 3:
        sll.display()
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
