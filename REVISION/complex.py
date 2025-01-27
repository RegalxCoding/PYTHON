class ComplexNo:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def __add__(self,other):
        n1=self.real+other.real
        n2=self.img+other.img

        print(ComplexNo(n1,n2).__str__())

    def __str__(self):
        return f"{self.real}+{self.img}i"

c1=ComplexNo(2,3)
c2=ComplexNo(4,5)
c3=c1+c2