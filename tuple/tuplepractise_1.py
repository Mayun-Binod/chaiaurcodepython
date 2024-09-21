# Create a tuple: Write a Python program to create a tuple with different data types (string, integer, list, etc.).
tuple=("hello",1,2,3,[1,2,3,4,5])
print(tuple)
print(type(tuple))

# Given a tuple t = (1, 2, 3, 4, 5), print the third element.
t=(1,2,3,4,5)
print(t[2])

# Unpacking tuples: Given a tuple t = ('apple', 'banana', 'cherry'), unpack the elements into three variables and print them.
t1=('apple','banana','cherry')
a,b,c=t1
print(t1)
print(a,b,c)

# Tuple slicing: Write a program to slice a tuple t = (1, 2, 3, 4, 5, 6, 7) from index 2 to 5.
t2=(1,2,3,4,5,6,7)
print(t2[2:5])

# Tuple methods: Given a tuple t = (10, 20, 30, 40, 20, 50), count how many times the value 20 appears.
t5=(10, 20, 30, 40, 20, 50)
print(t5.count(20))

# Tuple concatenation: Write a program to concatenate two tuples t1 = (1, 2, 3) and t2 = (4, 5, 6)
t6 = (1, 2, 3) 
t7 = (4, 5, 6)
t8=t6+t7
print(t8)

# Tuple of tuples: Create a tuple containing three tuples. Write a program to access the second element of the second tuple.
t9=((1,2),(3,4,8),(5,6))
t9[1][1]
print(t9)

# Tuple sorting: Given a list of tuples t = [(1, 'apple'), (3, 'banana'), (2, 'cherry')], sort the tuples based on the first element of each tuple.
t10 = [(1, 'apple'), (3, 'banana'), (2, 'cherry')]
t10.sort()
print(t10)

# Tuple immutability: How can you modify a tuple if tuples are immutable in Python? Write a program that demonstrates this concept by converting the tuple to a list, modifying it, and converting it back to a tuple.

# Original tuple
original_tuple = (1, 2, 3, 4, 5)

# Convert tuple to list
convert_list = list(original_tuple)
print(convert_list)  # Output: [1, 2, 3, 4, 5]

# Modify the list by appending a new element
convert_list.append(6)
print(convert_list)  # Output: [1, 2, 3, 4, 5, 6]

# Convert the list back to a tuple
new_tuple = tuple(convert_list)
print(new_tuple)  # Output: (1, 2, 3, 4, 5, 6)
