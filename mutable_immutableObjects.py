username="Binod"
username="saroj"
print(username)

# mutable dataTypes
# Definition: Mutable data types are those whose instances can be modified after they are created. This means you can change, add, or remove elements without creating a new object.

# 1.list
my_list = [1, 2, 3]
my_list.append(4)  # Adding an element
print(my_list)
# 2.Dictionary
my_dict = {"name": "Binod"}
my_dict["age"] = 25  # Adding a new key-value pair
print(my_dict)
# 3.Set
my_set = {1, 2, 3}
my_set.remove(2)  # Removing an element
print(my_set)
# 4.ByteArray
my_bytearray = bytearray([1, 2, 3])
my_bytearray[0] = 100  # Modifying a byte
print(bytearray)
# immutable dataTypes
# Definition: Immutable data types are those whose instances cannot be modified after they are created. Any modification results in the creation of a new object.

# 1.String
my_str = "hello"
my_str = "world"  # Creates a new string
print(my_str)
# 2.integer
x = 5
x = 10  # Creates a new integer object
print(x)
# 3.Float
y = 3.14
y = 2.71  # Creates a new float object
print(y)
# 4.Tuple
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # Raises an error

# 5.FrozenSet
my_frozenset = frozenset([1, 2, 3])
# my_frozenset.add(4)  # Raises an error

# 6.complex number
# Creating complex numbers
c1 = 3 + 4j  # 3 is the real part, 4 is the imaginary part
c2 = 1 + 2j

# Performing basic operations
sum_c = c1 + c2          # Addition
diff_c = c1 - c2         # Subtraction
prod_c = c1 * c2         # Multiplication
quot_c = c1 / c2         # Division

# Accessing real and imaginary parts
real_part = c1.real      # Output: 3.0
imaginary_part = c1.imag  # Output: 4.0

# Output results
print("Sum:", sum_c)          # Output: (4+6j)
print("Difference:", diff_c)   # Output: (2+2j)
print("Product:", prod_c)      # Output: (-5+10j)
print("Quotient:", quot_c)     # Output: (2.2+0.4j)
print("Real part:", real_part)  # Output: 3.0
print("Imaginary part:", imaginary_part)  # Output: 4.0
