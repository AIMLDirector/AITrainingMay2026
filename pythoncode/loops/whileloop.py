# while <condition>:
#     <action>

# user_list = ["admin", "kumar", "superuser"]
# user_role = ["student","admin", "operator"]
# while True:  # infinite loop or while loop with condition that always evaluates to true 
#     user_input = input("Enter the user name: ")
#     if user_input in user_list:
#         print("Welcome, ", user_input)
#         break
#     else:
#         print("Invalid user name, please try with other validations")
    

#     user_role = input("Enter the user role: ")
#     if user_role == "admin":
#         print("You have admin privileges")
#         break
#     elif user_role == "operator":
#         print("You dont have superuser privileges")
#         continue
#     else:
#         print("Invalid user role, please try again")

#     print("All the conditions are failed")
#     break

# import os
# while True:
#     memory_usage = os.popen("free -m").readlines()[1].split()[2]  # get the memory usage in MB
#     if int(memory_usage) > 80:
#         print("Memory usage is high, please check the system")
#         break
#     else:
#         print("Memory usage is normal, continue monitoring")
#         continue

# input_data = []
# while True:
#     user_input = input("Enter your requirement: ")
#     if user_input == "exit" or user_input == "quit":
#         print("Exiting the program")
#         break
#     elif user_input == "help":
#         print("This is a help message")
#         continue
#     else:
#         input_data.append(user_input)
#         print("Your requirement is added to the list")  
    
# max_retries = 3
# retry_count = 0

# while retry_count < max_retries:
#     user_name = input("Enter the user name: ")
#     if user_name == "admin":
#         print("Welcome, admin")
#         break
#     else:
#         print("Invalid user name, please try again")
#         retry_count += 1

    # if retry_count == max_retries:
    #     print("Maximum retries reached, you account has been locked")

for i in range(10):
    if i == 4:
        continue # skip the iteration when i is 4 and continue with the next iteration
    print(i)


for i in range(10):
    if i == 5:
        pass
    print(i) 


    

