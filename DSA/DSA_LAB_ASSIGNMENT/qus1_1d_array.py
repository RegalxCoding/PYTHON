def insert_element(array, element, position):
    if position < 0 or position > len(array):
        print("Invalid position! Please enter a valid position.")
    else:
        array.insert(position, element)
        print("Element inserted successfully.")

def delete_element(array, position):
    if position < 0 or position >= len(array):
        print("Invalid position! Please enter a valid position.")
    else:
        removed = array.pop(position)
        print(f"Element {removed} deleted successfully.")

def remove_duplicates(array):
    return list(set(array))

def display_menu():
    print("\nMenu:")
    print("1. Insert an element")
    print("2. Delete an element")
    print("3. Remove duplicate elements")
    print("4. Exit")
    
def main():
    array = []
    while True:
        display_menu()
        choice = int(input("Enter your choice (1/2/3/4): "))
        
        if choice == 1:
            element = int(input("Enter the element to insert: "))
            position = int(input("Enter the position to insert at (0-based index): "))
            insert_element(array, element, position)
            print("Current Array:", array)
            
        elif choice == 2:
            position = int(input("Enter the position to delete (0-based index): "))
            delete_element(array, position)
            print("Current Array:", array)
            
        elif choice == 3:
            array = remove_duplicates(array)
            print("Duplicates removed successfully.")
            print("Current Array:", array)
            
        elif choice == 4:
            print("Exiting the program. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
