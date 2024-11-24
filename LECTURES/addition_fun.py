#local variable scope declared and used within the block
def add():
    a=10
    b=20
    print(a+b)
add()


# def sub():
#     print(a-b)
# sub()

#global variable
msg="Hello"
def greet(name):
    print(name,msg)
greet("Sanji")

def hello():
    print(msg)

#nested function
a=23
def outer_fun():
    def inner_fun():
        a=777
        print("value of a:",a)
    inner_fun()#scope of inner function is only inside outerfunction
outer_fun()

def outer():
    msg="hello"
    def inner():
        #nonlocal allow to modify a variable from the outer function within the 
        #nested function but still it is not a global
        nonlocal  msg
        print(msg)
    inner()
    print(msg)
outer()

c=1 #cannot modify value of global variable
def add():
    global c
    c=c+2
    print(c)
add()

#recursion