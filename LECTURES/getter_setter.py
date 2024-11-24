class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def get_l(self):
        return self.l
    def get_b(self):
        return self.b
    def set_l(self,l):
        self.l=l
r1=Rectangle(4,5)
r1.set_l(45)
