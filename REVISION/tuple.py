import sys
t1=(1,2,3,4,3,2,20,2,2)
# print(t1)

# print(t1.count(2)) #count() counts no. of times item occurs

# tuple12=('rushabh')
# print(max(tuple12))

#change tuple values , first convert tuple into list
# tuple1=(1,2,3,4,5)
# y=list(tuple1)
# print(y)
# y.insert(1,"kiwi")
# x=tuple(y)
# print(x)

# a,b,c=(1,2,3)
# print(a,"",b,"",c)
# b=10
# print(a,b,c)

str="Rushabh"
print(sys.getsizeof(str))
b=bytes("Rushabh",'utf-8')
print(sys.getsizeof(b))
print(str[6])
