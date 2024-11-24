l1=[1,3,"Rushabh","Rohit",4.5]
#print(type(l1))

#inside list there is another list called nested list
l2=[4,5,l1,[12,13,14],True]
# print(l2)
# print(l2[1:3]) # start index 1 but excluding 3rd index
# print(l1[:4]) #start index from 0 to index 4[excluded]

# print(l1[-4:-1]) #start from -4 to index -1[excluded]

# print(l1[::-1]) #traversing list from end

# l1[1]="MCA"
# print(l1) #Change item value

# l1.insert(1,"MBA")
# print(l1) #now we have inserted item at pos 1 and other items shifted to next postion

#sort
# l3=[1,2,3,4,5]
# l3.sort(reverse=True)
# print(l3)

# list7=[1,2,3,4,5]
# #to extract all element of list
# x=list7[:]
# print(x)
# print(id(list7),id(x))

#in this both the ids will be same
# a=[10,30,50,70]
# b=a
# print(a,b)
# print(id(a),id(b))
# a[2]=100
# print(a,b)
# #if changes in copy it will change in original
# b[2]=200
# print(a,b)

# l1=[3,10,5]
# l2=[3,5,15]
# print(l1+l2)

# #repitation
# l3=[5,7]
# print(l3*5)

#-----loop through for loop
# l1=[1,3,"Rushabh","Rohit",4.5]
# for i in l1:
#     print(i)

#-----loop through index numbers
# for i in range(len(l1)):
#     print(l1[i])

#using while loop
i=0
while i<len(l1):
    print(l1[i])
    i+=1