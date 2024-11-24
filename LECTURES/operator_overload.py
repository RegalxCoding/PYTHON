a=10
b=20
print(int.__add__(a,b))
print(a+b)
x="Rushabh"
y="Jod"
print(str.__add__(x,y))
#__add__ never gonna work with object so
#we have to use operator overloading
#python do return multiple values but it can be tuple or list
class Add_Sub:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
       n1=self.x+other.x
       n2=self.y+other.y
       return (n1,n2)
    def __sub__(self,other2):
        m1=self.x-other2.x
        m2=self.y-other2.y
        return [m1,m2]
a1=Add_Sub(5,10)
a2=Add_Sub(10,15)
a3=a1+a2
print("Addition of a1 and a2:",a3)
m1=Add_Sub(10,20)
m2=Add_Sub(4,6)
m3=m1-m2
print("Subtraction of m2 and m2:",m3)
