#the ability to use a single type of entity, like a method, operator, 
# or object, to represent multiple types in different contexts.
#1.METHOD OVERLOADING AND OPERATOR OVERLOADING
#BUT python doesnt suppoRt 'METHOD OVERLOADING
def add(a,b):
    return(a+b)
def add(a,b,c):
    return(a+b+c)
print(add(4,5,7))
#if we write same name method whatever the last one it could be excepted

class addition:
    def add(self,a,b):
        return(a+b)
    def add(self,a,b,c,d):
        return(a+b+c+d)
class addition_one(addition):#here inheritance is compulsory
    def add(self,a,b,c):
        return(a,b,c)
obj=addition_one()
print(obj.add(5,6,7))

