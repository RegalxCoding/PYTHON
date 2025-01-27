class complexNo:
    def __init__(self,img,real):
        self.img=img
        self.real=real
    
    def __add__(self,other):
        n1=self.real+other.real
        n2=self.img+other.img

        print(complexNo(n1,n2).__str__())

    def __str__(self):
        return f"{self.real}+{self.img}i"
    
c1=complexNo(4,10)
c2=complexNo(5,10)
c3=c1+c2