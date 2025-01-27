class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)
        else:
            print("Duplicate keys are not allowed.")

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            print("Key not found.")
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children
            min_larger_node = self._find_min(node.right)
            node.key = min_larger_node.key
            node.right = self._delete(node.right, min_larger_node.key)

        return node

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def traverse_inorder(self):
        result = []
        self._traverse_inorder(self.root, result)
        return result

    def _traverse_inorder(self, node, result):
        if node:
            self._traverse_inorder(node.left, result)
            result.append(node.key)
            self._traverse_inorder(node.right, result)

# Menu-driven program
if __name__ == "__main__":
    bst = BinarySearchTree()

    while True:
        print("\nBinary Search Tree Operations:")
        print("1. Insert")
        print("2. Delete")
        print("3. Traverse (In-order)")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            key = int(input("Enter the value to insert: "))
            bst.insert(key)
            print(f"{key} inserted.")
        elif choice == '2':
            key = int(input("Enter the value to delete: "))
            bst.delete(key)
        elif choice == '3':
            print("In-order traversal:", bst.traverse_inorder())
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
