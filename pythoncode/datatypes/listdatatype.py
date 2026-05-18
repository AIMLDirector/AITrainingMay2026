a = [1,2,3,10.5,"kumar",3j,True]
b = [1,1,1,2,2,2,3,3,3]

# list data types ites can be ordered,changeable and allows duplicate values
# list data type is mutable data type

c = [10,20,30,40,50] # index = 0,1,2,3,4 or -5,-4,-3,-2,-1
print(c)
print(c[0])
print(c[0:3])  # access the element using index
# adding Data to the list : append, insert, extend
c.append(60)   # append is used to add the element at the end of the list
print(c)
c.insert(2,25)  # insert is used to add the element at the specified index
print(c)
b.extend(a)
print(b)
b.extend(c)
print(b)

# Deleting the data in the list : remove, pop, clear, del
c.remove(30)
print(c)
c.pop(2)  # pop is used to remove the element at the specified index
print(c)
c.pop()   # pop is used to remove the last element of the list
print(c)
c.clear()  # clear is used to remove all the elements from the list
print(c)
del c  # del is used to delete the list
d = [10,20,50,30,40]
d.sort()  # sort is used to sort the elements of the list in ascending order
print(d)
d.sort(reverse=True)  # sort is used to sort the elements of the list in descending order
print(d)

