import sys
#tuple is sequence datatype and it also stores hetrogenous datastructure but tuples are immutable
#can't make changes in tuple ,tuplle cannot do 

tuple=(1,'rushabh',21,[1,2,3])
print(tuple)
print(type(tuple))
#if not multiple value then it will not be tuple but add ',' thenn it becomes tuple
tuple1=(10)
print(tuple1)
print(type(tuple1))

tuple2=(True)
print(type(tuple2))

tuple2=()
print(type(tuple2))

print(tuple[1])
print(tuple[3][1])
tuple[3][1]=41
print(tuple)

tuple10=(1,2,3,4,2)
print(max(tuple10))
print(min(tuple10))
print(len(tuple10))

print(tuple10.count(2))

tuple12=('rushabh')
print(max(tuple12))

t=([1,2,3],[4,5,6])
print(max(t[1]))

a,b,c=(1,2,3)
print(a,"",b,"",c)
b=10
print(a,b,c)
#string and bytes are both immutable
str="nishant"
print(sys.getsizeof(str))
b=bytes("nishant",'utf-8')
print(sys.getsizeof(b))
print(str[6])

print(b.index(b't'))

#using bytearray we can change value of string
bb=bytearray("Nishant",'utf-8')
bb[0]=97
print(bb)