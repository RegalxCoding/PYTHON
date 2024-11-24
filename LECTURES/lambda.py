from functools import reduce
def square(n):
    res=n*n
    print("Square of number:",res)
square(5)
#lambda called anonymous
#in lambda only single expression can be passed
y=lambda x:x*x
print("Square of number:",y(6))

m=lambda l,b:l*b
print("Division:",m(8,4))
print(m(4,5))

x=lambda n,m:n+m
print("Addition:",x(4,5))

l=[3,2,6,8,4,6,2,9]
l2=[]
def even(a):
    for i in a:
        if i%2==0:
            l2.append(i)
    return l2
        
a=even(l)
print(l)
print(a) 

#filter function
lst=[3,2,6,8,4,6,2,9]
even=filter(lambda x:x%2==0,lst)
print(list(even))

#map function has 2 , 1st paramter function itself 2nd sequence
even_no=[2,6,8,4,6,2]
double=list(map(lambda x:x*2,even_no))
print(double)

#reduce function
sum=reduce(lambda x,y:x+y,double)
print(sum)