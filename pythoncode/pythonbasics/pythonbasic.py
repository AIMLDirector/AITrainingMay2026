# input variables

name = str(input("what is your name: "))
age = int(input("what is your age: "))

# output parameters
# print("hello", name, "you are", age, "years old")
# print("hello " + name + " you are " + age + " years old")
print(f"hello {name} you are {age} years old")
print("hello {} you are {} years old".format(name, age))
print("hello %s you are %s years old" % (name, age)) 


print(name)

if age < 18:
    print(f"hello {name} you are {age} years old you cannot vote")
else:
    print(f"hello {name} you are {age} years old you can vote ")


def f1():
    a = 0  # local variable 
    print(f"the value of a is {a}")
    print(f"hello {name} you are {age} years old")

f1()

print(f"the value of a is {a}")

def f2():
    b = 2
    c=10

