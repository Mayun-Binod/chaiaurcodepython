# create a function that accepts any number of keywords arguments and prints them in the format.key:value
def print_info(name, age=18, city='Unknown'):
    print(f"Name: {name}, Age: {age}, City: {city}")

print_info(name="Binod", age=25, city="Kathmandu")
print_info(name="Alice", city="London")


def describe_pet(animal_type, pet_name, age=None):
    print(f"Animal Type: {animal_type}")
    print(f"Pet Name: {pet_name}")
    if age is not None:
        print(f"Age: {age}")

describe_pet(animal_type="Dog", pet_name="Buddy", age=5)
describe_pet(pet_name="Whiskers", animal_type="Cat")



def display_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

info = {'name': 'John', 'age': 30, 'city': 'Los Angeles'}
display_info(**info)
