# tuples are orders and immutable( unchangeable) data types. they are defined by using parentheses () and items are separated by commas.

# t1  = ()  - tuples
# f1()  -- function 

t1 = (1,1,1,2,3,4) # data of int, float, string, complex, boolean
user_name = ( "admin", "kumar", "superuser")
# with tuples we can only able to read the data 
print(t1[0])
print(t1[0:3])

# Set is unordered and unindexed data type. it is defined by using curly braces {} and items are separated by commas. sets are mutable data types but they do not allow duplicate values.

s1 = {1,2,3,4,5,5} # data of int, float, string, complex, boolean/ no duplicate values
print(s1)

l1 = [1,2,3,3,3,3,4,4,4,5,5] # data of int, float, string, complex, boolean/ duplicate values
print(l1)
l1 = set(l1) # converting list to set
print(l1)
l1 = list(l1) # converting set to list  
print(l1)