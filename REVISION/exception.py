try:
    n=int(input("enter a num:"))
    res=10/n
    print(res)
except ZeroDivisionError:
    print("cannot divide by zero")
else:
    print("division is successfull")
finally:
    print("this will always work")

