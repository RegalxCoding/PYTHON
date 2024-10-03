#list is a datastructure and is sequence datatype and contain hetrogenous
#(any datatype can be store in a list)
l1=[1,2,3,4,5]
print(l1)
#type is method which return what kind of datatype you store in list
print(type(l1))
#everything in a variable is objects
l2=[20,30,'rushabh',40,'rohit']
print(l2)
print(type(l2))
l3=[10]
print(l3)
print(type(l3))
#1:3  , 3 is not included
list=[1,'mca',10.4,True]
print(list[1])
print(list[1:3])
print(list[1::2])
#inside of list there is nanother list called nested list
list2=[10,'mca',True,5.3,[1,2,3]]
print(list2[4][2])
#list is mutuable means you can change value of list
list2[2]=False
print(list2)
print(list2[::-2])

#insert function 
list2.insert(1,'MBA')
print(list2)

#remove function
list2.remove(10)
print(list2)

#append
list2.append("Pass")
print(list2)
list5=[10,20,30]
#take all element as 1 element[]
list2.append(list5)
print(list2)

#extend
list3=[1,2,3]
list4=[4,5,6]

list3.extend(list4)
print(list3)

#reverse
list2.reverse()
print(list2)

#pop
list2.pop()
print(list2)

#sort
list6=[1,2,3,4,5]
list6.sort(reverse=True)
print(list6)


#del delete particular element in list 
del list6[2]
print(list6)

#clear the list
list6.clear()
print(list6)

list7=[1,2,3,4,5]
#to extract all element of list
x=list7[:]
print(x,list7)
#clone there woul4d be different address
print(id(list7),id(x))
#cloning is making the another copy of 1st list
list7[3]=21
print(list7)
print(x)

#in this both the ids will be same
a=[10,30,50,70]
b=a
print(a,b)
print(id(a),id(b))
a[2]=100
print(a,b)
#if changes in copy it will change in original
b[2]=200
print(a,b)
#it is called shallow copy where both the list having same address
#if changes making to original , copy will also get changed

#deep copy where changes not done in both

l1=[3,10,5]
l2=[3,5,15]
print(l1+l2)

#repitation
l3=[5,10]
print(l3*3)