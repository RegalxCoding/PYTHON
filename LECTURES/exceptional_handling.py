#abnormal input from user
try:
    a=10
    b=0
    divide=a/b
    print(divide)
except:
    print("divide by zero")

#write the code inside the try like that code 
#whose responsible for generating the exceptiion
#try and except in except write those statement that user can understand

def div(a,b):
    print(a/b)
try:
   # div(10/0)
    lst=[10,20,30,40]
    print(lst[5])
except ZeroDivisionError:
    print("Divide by zeros")
except:
    print("for all")

#assert keyword if condition is true no problem
#if condition is false its going throw exception
#name of exception "assert error"

try:
    num=int(input("enter number:"))
    assert num%2==0
   
except:
    print("number is not an even")

else:
    rec=1/num
    print(rec)
finally:
    print("Fianlly block is executed") #use in connection closing