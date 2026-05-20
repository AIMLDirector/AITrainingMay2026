a = 1
b = 2
c = 3

if a > b:
    print("a is greater than b")

if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")

if a > b:
    print("a is greater than b")
elif a > c:
    print("a is greater than c")
else:
    print("a is not greater than b and c")


if a > b and a > c:
    print("a is greater than b and c")
elif b > a and b > c:
    print("b is greater than a and c")
else:
    print("c is greater than a and b")

if a > b and a > c:
    print("a is greater than b and c")
elif b > a and b > c:
    print("b is greater than a and c")
elif c > a and c > b:   
    print("c is greater than a and b")
else:
    print("a, b and c are equal")


file_name = "ifloop.txt"

if file_name.endswith(".txt"):
    print("This is a text file")

if file_name.startswith("if"):
    print("This file name starts with if")


file_name_list = ["ifloop.txt", "ifcondition.py", "ifcondition.ipynb", "ifcondition.docx"]

file_text = []
file_pdf = []
file_other = []

for file in file_name_list:
    if file.endswith(".txt"):
        file_text.append(file)  
    elif file.endswith(".pdf"):
        file_pdf.append(file)
    else:
        file_other.append(file)

print("Text files: ", file_text)
print("PDF files: ", file_pdf)
print("Other files: ", file_other)

user_name = ["admin", "kumar", "superuser"]

if "admin" in user_name:
    print("admin is present in the user_name list")

user_name_input = input("Enter the user name: ")

if user_name_input == "admin" or  user_name_input == "superuser":
    user_password = input("Enter the password: ")
    print("with admin and superuser you can access the system")
else:
    print("with other user you cannot access the system")


import os

status_code = os.system("ping -n 1 google.com")

if status_code == 0:
    print("Google is reachable")
else:
    print("Google is not reachable")

   
#case1
# # file1 -- log  - if condition to check whether the log file has any error messages if yes then filter out the error messages
# line and store in error_log.txt other messages to be stored in info_log.txt


# file1.txt -- error_log.txt and info_log.txt 


#case 2
#  username and password as input incase if the username is capital convert to lower 

#  condition validation if the user name is admin  you are allow to login else not allow  
# when you type the password it should not be visible in the screen 





