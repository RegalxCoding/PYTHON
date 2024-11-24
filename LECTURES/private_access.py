class student:
    def __init__(self,name,roll):
        self.__name=name
        self.__roll=roll
    def show(self):#to access private variable outside the class 
        #we can access through using public method
        print("Name:",self.__name)
        print("Roll:",self.__roll)
    def _display(self):
        print("Name:",self.__name)
        print("Roll",self.__roll)
s1=student("karna",201)
s1.show()
s2=student("Arjun",202)
s2._display()