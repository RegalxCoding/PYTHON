def logger(fx):
    def wrapper(*args,**kwargs):
        print(f"arguments {args}, keyword arggument:{kwargs}")
        fx(*args,**kwargs)
    return wrapper
        

@logger
def add_num(a,b):
    print("addition",a+b)

add_num(5,10)