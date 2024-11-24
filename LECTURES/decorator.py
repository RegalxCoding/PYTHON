#do allow to change the behaviour of the existing function




def decor(func):
    def inner(x,y):
        if x<0:
            x=0
        if y<0:
            y=0
        return func(x,y)
    return inner
@decor
def add(a,b): 
    #add=decor(add)
    return(a+b)
print("addition is:",add(30,70))
print("addition is:",add(-10,20))

@decor
def sub(a,b):
    return(a-b)
print("subtraction is:",sub(-20,50))
print("subtraction is:",sub(50,70))

for i in range(1,201):
    print(i)
    i+=1