
def greet(fx):
    def mfx(*args,**kargs):
        print("good morning")
        fx(*args,*kargs)
        print("thanks for using this function")
    return mfx

@greet
def hello():
    print("hello rushabh")

def add(x,y):
    print(x+y)
     
hello()
greet(add)(1,2)

