n=int(input("enter number of terms:"))

if n<=0:
    print("please enter positive number")

a,b=0,1

for _ in range(n):
    print(a,end="")
    a,b=b,a+b

print()

