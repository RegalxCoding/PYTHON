#set is collection of hetrogenous data but cant have duplicate values
#no need of indexing to access values 
#set data does not follow any order

s1={10,20,'rushabh'}
print(s1)
s2={100,2000,'rushabh'}
print(s2)
#union
print(s1|s2)
print(s1.union(s2))


#intersection
print(s1&s2)
print(s1.intersection(s2))

#difference
print(s2-s1)
print(s1-s2)