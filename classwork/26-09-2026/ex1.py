# decorator - function that takes another function as an argument 
# and extends the behavior of the latter function without
# explicitly modifying it


import time

def profiling_decorator(func):
    def inner(*args,**kyargs):
        before=time.time()
        result = func(*args,**kyargs)
        diff=time.time()-before
        print(f"Time taken to execute the function {func.__name__} is {diff} seconds")
        return result
    return inner
@profiling_decorator
def printfuc():
    for i in range(5):
        time.sleep(1)
        print("Hello World")

printfuc()