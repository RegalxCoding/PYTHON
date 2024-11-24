#magic method also called dunder
def add(a,b):
    print("addition",a+b)
add.__call__(40,30)

#__call__() inside the python class
class Demo:
    def __init__(self):
        print("this is constructor")
    def __call__(self):
        print("Call Method")
d=Demo()
d()

class Student:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def __call__(self,college):
        #binding function and variable as single unit
        print("Id:",self.id,"Name:",self.name)
        self.college=college
        print("College:",{college})
s1=Student(101,"Rushabh")
s1("DYPIMR")


class emp:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name)
class dept(emp):
    def __init__(self,n):
        emp.__init__(self,n)
d=dept("SANJI")
d.show()

class student:
    def __init__(self,name):
        self.name=name
    def disp(self):
        print("Name:",self.name)
class marks:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def disp2(self):
        print("marks1:",self.m1,"marks2:",self.m2,"marks3:",self.m3)
class result(student,marks):
    def __init__(self,n,m1,m2,m3):
        student.__init__(self,n)
        marks.__init__(self,m1,m2,m3)
r=result("Zoro",50,60,70)
r.disp()
r.disp2()
