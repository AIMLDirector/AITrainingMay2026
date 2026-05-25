# def func1():
#     print("first function")

# # functions with arguments/parameters

# def func2(name):   # parameter
#     print("hello " + name)

# a = 1   # parameter or variable 

# # func1()
# # func2("python")  # argument is the value passed to the function when it is called, here "python" is the argument for parameter name in func2
# # func1()
# # func2("programming")


# def func3(name1:str="kumar", name2:str= "sam"): 
#     fname1 = name1 
#     fname2 = name2 
#     print("hello " + fname1)
#     print("hello " + fname2)

# # func3()
# # func3("python", "programming")
# # func3(10,20)


# def func4(*args):
#     print(args) 
#     print(type(args)) # args is a tuple
#     for i in args:
#         print(i)

# # func4(1,2,3,4,5)
# # func4("python", "programming", "language")

# def func5(**kwargs):
#     print(kwargs)
#     print(type(kwargs)) # kwargs is a dictionary
#     for key, value in kwargs.items():
#         print(key, value)

# func5(name="python", type="programming language")


# def func5(fname:str, lname:str) -> str:
     
#     print(fname + " " + lname)
#     return f"{fname} {lname}"


# output = func5("python", "programming")
# print(output)



# def func6(a:int, b:int):
#     c = a+b 
#     return c

# output1 = func6(2,3)
# print(output1)

import time

def time_decortor(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

# def time_decorator(func):
#         start_time = time.time()
#         result = func(*args)
#         end_time = time.time()
#         print(f"Execution time: {end_time - start_time} seconds")
#         return result


@time_decorator
def func10(list1):
    total = 0
    for i in list1:
        if isinstance(i, int):
            total += i
    return total


output= func10([1,2,3,"ss",5])
print(output)

# func10 = time_decorator(wrapper(func10))  # this is how the decorator works without using @ symbol

@time_decorator
def func11():
    pass

#decoraters are used to modify the behavior of a function without changing its code. They are often used for logging, timing, and access control.





    