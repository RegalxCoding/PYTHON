#reusability
# class parent:
#     def show(self):
#         print("parent")
# class child(parent):
#     def display(self):
#         print("child")
# c=child()
# c.show()
# c.display()
#multilevel
#student parent and exam child and result another child
class student:
    rollno=1
    name="Rushabh"
    study="MCA I"
    def show(self):
        print("Rollno-",self.rollno,"Name-",self.name,"Class-",self.study)
class exam(student):
    subject="Maths"
    Marks=200
    def disp(self):
        print("Subject-",self.subject,"Marks-",self.Marks)
class result(exam):
    def display(self):
        print("Result of student\n")
d=result()
d.display()
d.show()
d.disp()

#multiple inheritance
class parent1:
    def show(self):
        print("parent1")
class parent2:
    def show(self):
        print("parent 2")
class child(parent1,parent2):#jisko pahele likhoge uska function call hoga even name same raha toh [MRO[METHOD RESOLVE ORDER]]
    def show(self):
        print("child")
c=child()
c.show()
# c.display()

# class sbi:
#     p=2000
#     r=7
#     t=2
#     rate_of_intereset=p*r*t
#     def show(self,r,y):
#         rate=self.r*self.y*7/100
#         print(rate)
# class hdfc:
#     def disp(self,r,y):
#         rate2=self.r*self.y*7.25/100
#         print(rate2)
# class fd(sbi,hdfc):
#     pass
# f=fd()
# f.show(4000,5)
# f.disp(5000,6)

class student:
    def __init__(self):
        print("student")
class exam(student):
    def __init__(self):
        print("child")
        super().__init__()
       
e=exam()

#Q