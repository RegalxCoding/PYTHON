from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")

db=client["user_data"]
collection=db["profile"]

def user_input():
    n=int(input("enter how many records to inserts:"))
    for _ in range(n):
        name=input("enter name:")
        age=int(input("enter age:"))

        doc={"name":name,"age":age}
        collection.insert_one(doc)
        print("data inserted successfully")

def display():
    for d in collection.find():
        print(d)

def update_data():
    update_name=input("enter name to usert whose data you want to update:")
    update_age=int(input("enter age to update:"))

    res=collection.update_one({"name":update_name},{"$set":{"age":update_age}})

    if res.matched_count>0:
        print(f"data for {update_name} is updated successfully")
    else:
        print("no data to update")


    
def main():
    user_input()
    display()
    update_data()

if __name__=="__main__":
    main()
