# def generate_num(n):
#     for i in range(1,n+1):
#         yield i

# # num=generate_num(5)

# print("generatred num:")
# for n in generate_num(5):
#     print(n)


# def even_odd(n):
#     for i in range(1,n+1):
#         if i%2==0:
#             yield f"{i} is even"
#         else:
#             yield f"{i} is odd"


# for n in even_odd(10):
#     print(n)

def prime(n):
    for num in range(2,n+1):
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                break
        else:
            print(f"{num} is prime")
        
n=int(input("enter a num:"))
prime(n)