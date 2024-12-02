# Initial dictionary
my_dict = {}

# Function to add an item
def add_item(key, value):
    if key in my_dict:
        print(f"Key '{key}' already exists. Use update to modify it.")
    else:
        my_dict[key] = value
        print(f"Added: {key} -> {value}")

# Function to read an item
def read_item(key):
    if key in my_dict:
        print(f"{key} -> {my_dict[key]}")
    else:
        print(f"Key '{key}' does not exist.")

# Function to update an item
def update_item(key, value):
    if key in my_dict:
        my_dict[key] = value
        print(f"Updated: {key} -> {value}")
    else:
        print(f"Key '{key}' does not exist. Use add to create it.")

# Function to delete an item
def delete_item(key):
    if key in my_dict:
        del my_dict[key]
        print(f"Deleted: {key}")
    else:
        print(f"Key '{key}' does not exist.")

# Menu for CRUD operations
while True:
    print("\nChoose an operation:")
    print("1. Add item")
    print("2. Read item")
    print("3. Update item")
    print("4. Delete item")
    print("5. Display dictionary")
    print("6. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        key = input("Enter the key: ")
        value = input("Enter the value: ")
        add_item(key, value)
    elif choice == 2:
        key = input("Enter the key to read: ")
        read_item(key)
    elif choice == 3:
        key = input("Enter the key to update: ")
        value = input("Enter the new value: ")
        update_item(key, value)
    elif choice == 4:
        key = input("Enter the key to delete: ")
        delete_item(key)
    elif choice == 5:
        print("Current Dictionary:", my_dict)
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
