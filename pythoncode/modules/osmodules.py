# in build modules : os, sys, datetime, re,json, csv,random, subprocess, argparse, logging,http

# os module : operating system related functionality - file and directory management, environment variables, process management, path manipulation, etc.

import os
# get current working directory
print(os.getcwd())
print(os.listdir())  # list the files and directories in the current working directory
# print(os.mkdir("test_dir"))

# if os.path.exists("test_dir"):
#     print("Directory exists and deleted")
#     os.rmdir("test_dir")
# else:
#     print("Directory does not exist and created")
#     os.mkdir("test_dir")

os.system("netstat -nr")
user_name = os.getuid()  # get the user id of the current user
print(user_name)

if os.path.exists("test.txt"):
    file_size = os.path.getsize("test.txt")  # get the size of the file in bytes    
    print(f"File size: {file_size} bytes")
   
os.environ["default_name"] = "admin"  # set an environment variable
print(os.environ["default_name"])  # get the value of an environment variable



