try:
    print(10/0)  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print("Error: Cannot divide by zero.")
    print(f"Exception message: {e}")


# num = int(input("Enter a number: "))  # This may raise a ValueError if input is not a valid integer
# print(f"You entered: {num}")

try:
    num = int(input("Enter a number: "))  # This may raise a ValueError if input is not a valid integer
    print(f"You entered: {num}")
except ValueError as e:
    print("Error: Invalid input. Please enter a valid integer.")
    print(f"Exception message: {e}")


try:
    age = 10
    message = " i am " + age + " years old"  # This will raise a TypeError because age is an integer
except TypeError as e:
    print("Error: Cannot concatenate string and integer.")
    print(f"Exception message: {e}")


try:
    import pands  # This will raise a ModuleNotFoundError because 'pands' is not a valid module
except ModuleNotFoundError as e:
    print("Error: Module not found.")
    print(f"Exception message: {e}")

import os
file = None

# when finally we will use : open a file, connecting to the db and execute some command and close the connection to the db or close the file
try:
    file = open("non_existent_file.txt", "r")  # This will raise a FileNotFoundError
except FileNotFoundError as e:
    print("Error: File not found.")
    print(f"Exception message: {e}")
else:
    os.system("echo 'This is a test.' > non_existent_file.txt")
    file = open("non_existent_file.txt", "r") 
finally:
    print("This block will always execute, regardless of exceptions.")
    if file is not None:  
        file.close()


