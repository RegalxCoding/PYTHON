#the standard lock object does not care which thread currently 
#holding the lock. If the lock is being hold by one thread and 
#another thread wanted to acquire the lock, it will be blocked even
#it will be the same thread

#mutlithreading is a way to achieve multitasking
#concept of thread is use

#Solution:- Reentrant
#at a time one thread only  access one person


#factorial program to understand threading

from threading import *
import time
# l=RLock()
# def fact(n):
#     l.acquire()
#     if n==0:
#         res=1
#         return res
#     else:
#         result=n*fact(n-1)
#         l.release()
#         return result
# def show_factorial(n):
#     print(f"Factorial of {n} is {fact(n)}")

# #t1 = Thread(target=show_factorial, args=(5,))
# t1 = Thread(target=show_factorial, args=(5,))
# t1.start()

# t2=Thread(target=show_factorial, args=(6,))
# t2.start()

#semaphore
s=Semaphore(2)#how many thread can be access at a time
def wish(name,age):
    for i in range(5):
        s.acquire()
        print("NAME-",name,"AGE-",age)
        time.sleep(5)
        s.release()

t1=Thread(target=wish,args=("Rushabh",20))

t2=Thread(target=wish, args=("Rohit",21))
# t2.start()
t3=Thread(target=wish, args=("aman",21))
t4=Thread(target=wish, args=("sahil",21))
t5=Thread(target=wish, args=("sambha",21))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

