# external modules 
import pandas
import numpy
# Internal modules
import os
import sys
import datetime
import math

# enabling the environment files and variables

openai_api_key = os.getenv("OPENAI_API_KEY")
username = os.getenv("oracle_user")
password = os.getenv("oracle_password")

a = 1  # integer variable
b = 2.5 # float variable
c = "Hello, World!" # string variable

Name = input("what is your name: ")

# function, class, loop, conditional statements, and data structures


if a == 1:
    print("a is equal to 1")

for i in range(5):
    print(i)

def fun1(name = Name):
    print("This is a function coding and my name is " + name)


# Execution of the function or class 

fun1()




