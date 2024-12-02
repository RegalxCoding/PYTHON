import pymongo

if __name__=="__main__":
    # print("welcome to pymongo")
    client=pymongo.MongoClient("mongodb://localhost:27017")#connection string connects local db
    # print(client)
    db=client['rushabh']        #db created ,now we have create collection
    collection=db['mySampleCollection']
    one=collection.find_one({'_id':2})
    print(one)
    allDocs=collection.find({'name':'Aman'},{'name':1,'_id':0})
    for i in allDocs:
        print(i)

    allDatabase=client.list_database_names()
    print(allDatabase)