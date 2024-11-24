dict1={"name":"Rishi","age":20,"occupation":"pilot"}
print(dict1)

# print(dict1.pop("name"))#delete the key and display rest data and value
# print(dict1)

# # x=dict1.keys() #getting keys
# # print(x)
# # print(dict1.values())  #getting values

# #adding a new item to list
# dict1["location"]="Pune"
# print(dict1)

# x=dict1.items()
# print(x)  #getting items

#creating nested dictionaries
d1={"child1":{
    "name":"Zoro","age":24
},
"child2":{
    "name":"Sanji","age":29
},
"child3":{
    "name":"Ussop","age":22
}
}
print(d1)
print(d1["child2"]["name"])
print(d1["child3"]["name"])