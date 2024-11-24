def Hello():
    print("Hello Sanji")
Hello()

def Hello(name):
    print("hello Chalo",name)
Hello("MCA")

def Add(a,b):
    print("Addition:",a+b)
Add(5,3)

def greet(name,msg="hello"):
    print(msg,name)
greet("Sanji")

def circle(radius):
    area=3.14*radius*radius
    print("area of circle:",area)
circle(3)

def rect(length,breadth):
    return length*breadth
x=rect(5,3)
print("ARea of rectangle:",x)

def fact(num):
    f=1
    i=1
    for i in range(i,(num+1)):
        f=f*i
        i+=1
    print("fact:",f)
fact(0)




