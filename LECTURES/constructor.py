#name is same no. of arg are different is called constructor overloading
class student:
    def __init__(self):
        print("constructor")
    def __init__(self):
        print("constructor 1")
    def __del__(self):
        print("destructor")
s1=student()
s2=student()
#class variable
#class method
#instance variable
class emp:
    company="pinterest"#a class variable is variable of class and not use by self
    def __init__(self,name,sal):#self addr of current object it is instance of class
        self.name=name #instance variable
        self.sal=sal
    def show(self):
        print(self.name,self.sal)
        #method not associated by object is called function
    def display():
        print(emp.company)
    #1st paramater is cls if u want to make class method
    #instance method pass self
    #decorator
    @classmethod
    def display(cls):
        print(cls.company)
    @staticmethod
    def display():
        print("static funtion")
e1=emp("rushabh",10000)
e1.show()
print(e1.company)
# e2=emp("rohit",5000)
# e2.show()
# print(e2.company)
#tech by name of class we should call class variable
# print(emp.company)
emp.display()
emp.display()