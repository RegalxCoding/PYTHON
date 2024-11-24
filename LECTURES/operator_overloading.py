class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return(self.a+self.b)
    def add2(self):
        return(self.a+self.b)
obj1=A(10,20)
obj2=A(30,40)

obj3=obj1.add()
obj4=obj2.add()
obj5=obj3+obj4
print(obj5)

obj1=A("Rushabh","Tak")
obj2=A(" study","in MCA")
obj3=obj1.add2()
obj4=obj2.add2()
obj5=obj3+obj4
print(obj5)