import time
def profiling(func):
    def wrapper(*args, **kwargs):    # kwargs for unlimited number of keyword arguments
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper

#A decorator is essentially a function that takes another function as an argument, adds some functionality, and returns a new function.

@profiling    # @profiling is a decorator that wraps the add function to measure its execution time
def add(*args): # *args for unlimited number of arguments
    time.sleep(2)
    return sum(args)
    
@profiling
def display_info():
    for i in range(2):
        time.sleep(1)
        print("info displayed")

add(1, 2, 3, 4, 5)
display_info()
print("Calling using the function directly:")
profiling(add(1, 2, 3, 4, 5))  # Calling the add function directly without using the decorator
profiling(display_info())  # Calling the display_info function directly without using the decorator

# @add  
# c=(1,2,3,4,5)  this wont work because decorators are only applied to fucntions and not variables. only takes functions as parameters.

