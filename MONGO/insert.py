import pymongo

if __name__=="__main__":
    # print("welcome to pymongo")
    client=pymongo.MongoClient("mongodb://localhost:27017")#connection string connects local db
    # print(client)
    db=client['rushabh']        #db created ,now we have create collection
    collection=db['mySampleCollection']
    # dict1={'name':'Rushabh',
    #        'marks':80,
    #        'phone':98376282929}
    # collection.insert_one(dict1)

    # dict2={'name':'Rohit','marks':89,'phone':832829282}
    # collection.insert_one(dict2) 
    l1=[
        {'_id':1,'name':'Rushabh','location':'nagar','age':21},
        {'_id':2,'name':'Aman','location':'nagar','age':22},
        {'_id':3,'name':'Sahil','location':'nagar','age':23}
    ]
    collection.insert_many(l1)
    
    
