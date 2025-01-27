from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017/")

db=client["mydb"]
collection=db['mycollect']

def insert_stu():
    name=input("enter name:")
    mrks=int(input("enter marks:"))
    stu_data={'name':name,'marks':mrks}
    collection.insert_one(stu_data)
    print("data inserted successfully")

def display_high_scorers():
    print("\nStudents with marks >= 80:")
    high_scorers = collection.find({"marks": {"$gte": 80}})
    for student in high_scorers:
        print(f"Name: $student['name'], Marks: $['marks']")

def update_data():
    name_update=input("etner name to update")
    mrks_update=input("etner new marks of student:")
    res=collection.update_one(
        {"name":name_update},
        {"$set":{"mrks":mrks_update}}
    )


if __name__=="__main__":
    while True:
        print("\n1. Insert Student Data")
        print("2. Display Students with Marks >= 80")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            insert_stu()
        elif choice ==2:
            display_high_scorers()
        elif choice ==3:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

              
