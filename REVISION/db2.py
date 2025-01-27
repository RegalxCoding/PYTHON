from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017/")

db=client['wifi']
collection=db['wifi_details']

def insert_data():
    name=input("enter wifi name:")
    price=int(input("enter wifi installation price:"))
    wifi_data={"wifi_name":name,"wifi_price":price}

    collection.insert_one(wifi_data)
    print("data inserted successfully")

def read_data():
   disp=collection.find({"wifi_price":{"$gt":500}})
   print("wifi name with price greater than 500:")
   for d in disp:
      print(f"Name:{d['wifi_name']},Price:{d['wifi_price']}")

def update_data():
    name=input("enter wifi to update:")
    price_to_update=int(input("enter new price:"))

    res=collection.update_one(
        {"wifi_name":name},
        {"$set":{"wifi_price":price_to_update}}
    )
    if res.matched_count>0:
        if res.modified_count>0:
            print("data updated successfully")
        else:
            print("data is upto-date")
    else:
        print("no matching data found to update")
    
def del_data():
    name_to_del=input("entet wifi name to delet:")
    res=collection.delete_many({"wifi_name":name_to_del})
    if res.deleted_count>0:
        print("data deleted successfully")
    else:
        print("no matching data found to delete")
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
        elif ch==4:
            del_data()
        
        else:
            print("invalid choice")

