#Write a Python program to create a dictionary with keys as names and values as ages.
dict={
    "name":"Binod",
    "age":23
}
print(dict)

# Given the dictionary d = {'apple': 1, 'banana': 2, 'cherry': 3}, access and print the value associated with the key 'banana'.
d = {'apple': 1, 'banana': 2, 'cherry': 3}
print(d['banana'])

# Write a program to add a new key-value pair to a dictionary d = {'a': 10, 'b': 20}.
d1= {'a': 10, 'b': 20}
d1.update({'c':30})
print(d1)
# another method
d1['d']=40
print(d1)

# Check if a key exists: Write a program to check if a key 'orange' exists in the dictionary d = {'apple': 1, 'banana': 2, 'cherry': 3}.
# Given dictionary
d2 = {'apple': 1, 'banana': 2, 'cherry': 3}
if 'orange' in d2:
    print("Key 'orange' exists in the dictionary.")
else:
    print("Key 'orange' does not exist in the dictionary.")

# Update dictionary: Given d = {'name': 'Alice', 'age': 25}, update the age to 26 and add a new key 'city' with value 'New York'.
d4 = {'name': 'Alice', 'age': 25}
d4.update({'age':26,'city':'New York'})
print(d4)
# another method
d4['age']=26
d4['city']='New York'
print(d4)

# Write a program to iterate through the dictionary d = {'x': 1, 'y': 2, 'z': 3} and print each key-value pair.
d5 = {'x': 1, 'y': 2, 'z': 3}
for key, value in d5.items():
    print(f"Key: {key}, Value: {value}")


#Create a nested dictionary where each key represents a person, and each value is a dictionary with keys 'age' and 'city'. Access the city of a specific person.
d7 = {
    "Alice": {
        "age": 30,
        "city": "KTM"
    },
    "Bob": {
        "age": 25,
        "city": "Pokhara"
    },
    "Charlie": {
        "age": 28,
        "city": "Bhaktapur"
    }
}

print(d7["Alice"]["city"])

