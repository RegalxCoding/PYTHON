print(__name__)
#abstract class
#hide the detailing 
#only declaration not defination
#Abstract class which hide the implementation and atleast have 1 abstract method
#ABC [Abstract Base Class]
#we cannot create object of abstract class

# from abc import ABC,abstractmethod
# class Friend(ABC):
#     @abstractmethod
#     def role(self):
#         pass
# class Rakesh(Friend):
#     def role(self):
#         print("Rakesh is a developer")
# class analysis(Friend):
#     def role(self):
#         print("Rakesh is analyist")

from abc import ABC,abstractmethod
class RBI(ABC):
    @abstractmethod
    def ROI(self,r,i):
        pass
class SBI(RBI):
    def ROI(self,r,i):
        ans=r*i
        print("Rate of Interest:",ans)
class AXIS(RBI):
    def ROI(self,r,i):
        res=r*i
        print("Rate of Interest ",res)
s=SBI()
s.ROI(1000,7)
a=AXIS()
a.ROI(2000,8)