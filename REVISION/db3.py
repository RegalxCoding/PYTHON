from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017/")

db=client['school']
collection=db['students']

def insert_data():
    name=input("enter name of student:")
    age=int(input("enter age of student:"))
    marks=int(input("enter marks of student:"))

    stu_data={"name":name,"age":age,"marks":marks}

    collection.insert_one(stu_data)
    print("data inserted successfully")

def read_data():
    res=collection.find({"marks":{"$gte":80}})

    for r in res:
        print(f"Name:{r['name']},Age:{r['age']},marks:{r['marks']}")


def update_data():
    name=input("enter name to update:")
    updated_age=int(input("enter new age of student:"))

    res=collection.update_one(
        {"name":name},
        {"$set":{"age":updated_age}}
    )
    if res.matched_count>0:
        if res.modified_count>0:
            print("data modified successfully")
        else:
            print("data up to date")
    else:
        print("no data to updation")



if __name__=="__main__":
     while True:
        print("Option\n1.insert data\n2.display data\n3.update data\n4.delete data")
        ch=int(input("enter your choice:"))

        if ch==1:
            insert_data()
        elif ch==2:
            read_data()
        elif ch==3:
            update_data()
        # elif ch==4:
        #     del_data()
        
        else:
            print("invalid choice")