#*args means variable length args
#the * arguments allow to pass the variable number
#of non keywords
def add(*num):
    sum=0
    for i in num:
        sum+=i
    print("sum of numbers:",sum)

add(1,2,3,4,5)
add(4,5)

#to pass keyword as an argument use **kwargs
def intro(**data):
    for key,value in data.items():
        print(key,value)
intro(fname="Rushabh",sname="Tak",age=22)
