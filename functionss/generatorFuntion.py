# generator function with yield
# create a generator function that yields even number up to a specified limit
def even_numbers(limit):
    for num in range(0, limit + 1, 2):  # Start from 0 and increment by 2 (even numbers)
        yield num

# Usage
for even in even_numbers(20):
    print(even)
