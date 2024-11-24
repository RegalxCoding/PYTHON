from abc import ABC,abstractmethod,ABCMeta
class emp(metaclass=ABCMeta):
    @abstractmethod
    def show(self):
        pass
#public private and protected access specifier
#public variable can be access out of the class as well as inside the class
# class student:
#     def __init__(self):
#         self.name="RushabhJod"
#         self.age=21
# s1=student()
# print("Name of Student:",s1.name)
# print("Age:",s1.age)
# print("ListField",dir(s1))#dir is a directory

#protected variable
# class student:
#     def __init__(self):
#         self._name="RohitXZoro"
#         self._rollno=21
# class exam(student):
#     def _show(self):
#         print("Name of Student:",self._name)
# class res(exam):
#     def display(self):
#         print("roll no:",self._rollno)

# e1=exam()
# e1._show()
# r1=res()
# r1.display()
# r1._show()

class student:
    _name="shreyas"
    _roll=21
    def __init__(self,name,roll):
        self._name=name
        self._roll=roll
    def _display(self):
        print(self._name)
        print(self._roll)
class MCA(student):
    def displayMCA(self):
        self._display()
s=student("karan",102)
m=MCA()
m.displayMCA()