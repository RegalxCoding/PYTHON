#in operator overloading always work with the objects
class complexno:
    def __init__(self,img,real):
        self.real=real
        self.img=img
    def __add__(self,other):
        n1=self.real+other.real
        n2=self.img+other.img
        
        print(complexno(n1,n2).__str__())
    def __str__(self):
        return f"{self.real}+{self.img}i"
c1=complexno(5,10)
c2=complexno(10,20)
c3=c1+c2
#print(c3.__str__())
        