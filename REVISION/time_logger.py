import time

def execution(fx):
    def wrapper(*args,**kwargs):
        s_time=time.time()
        res=fx(*args,**kwargs)
        e_time=time.time()
        ex_time=e_time-s_time
        print(ex_time)
        return res
    return wrapper
    
@execution
def slow_execution():
    time.sleep(2)
    print("execution finished")

