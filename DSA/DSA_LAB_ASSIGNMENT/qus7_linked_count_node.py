# Algorithm to Count Number of Nodes in a Singly Linked List
# 1.Initialize a Counter: Start with a variable count set to 0.
# 2.Start Traversing: Assign the head of the linked list to a temporary pointer current.
# 3.Traverse the List:
# 4.While current is not None, increment the count by 1.
# 5.Move the pointer to the next node using current = current.next.
# 6.Return the Count: Once the traversal is complete, return the value of count.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, data):
        newNode = Node(data)
        if self.head is None:  # If list is empty
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode

    def countNodes(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

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
    print("2. Count Nodes")
    print("3. Display List")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter data to add: "))
        sll.addNode(data)
    elif choice == 2:
        print(f"Number of nodes in the list: {sll.countNodes()}")
    elif choice == 3:
        sll.display()
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
