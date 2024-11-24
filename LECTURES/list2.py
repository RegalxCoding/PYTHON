# l1=[1,2,3]
# l2=[1,2,3]
# print(id(l1),id(l2))
# print(l1 is l2)
# #list behave ase object and obj create diff address you create new list and have a same num its addr will different
# print(l1==l2)

l1=[1,2,3,[4,2,3]]
print(id(l1))
print(id(l1[0]))
print("id of 2",id(l1[1]))
print(id(l1[2]))
print(id(l1[3]))
print("id of 2 inside nested list",id(l1[3][1]))
#when list is stored it takes address 