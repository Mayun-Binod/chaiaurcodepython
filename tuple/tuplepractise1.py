# A tuple in Python is an immutable, ordered collection of items. Unlike lists, tuples cannot be modified after creation. Tuples are defined by placing items inside parentheses () separated by commas.
# tuple=tuple()
# print(tuple)

tuple_1=(1,2,3,4,4,4,5)
print(tuple_1)
print(type(tuple_1))
tuple_2=(1,)
print(tuple_2)
print(type(tuple_2))
tuple4=1,2,3,4
print(tuple)
print(type(tuple4))

list=[1,2,3,4,5]  #comes in tuple
t=tuple(list)
print(t)

set={1,2,3,45,6}  #comes in tuple
t1=tuple(set)
print(t1)

# Example 3: Tuple Without Parentheses (Packing)
# You can also create a tuple without using parentheses:

another_tuple = 10, 20, 30
print(another_tuple)


# Tuple unpacking allows you to assign the elements of a tuple to multiple variables in a single line. Here's how you can create a tuple and unpack it:

# Example 1: Tuple Unpacking

# Creating a tuple
my_tuple = (10, 20, 30)

# Unpacking the tuple into variables
a, b, c = my_tuple

print(a)  # Output: 10
print(b)  # Output: 20
print(c)  # Output: 30