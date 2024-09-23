# debugging function calls
# create a decorator to print the function name and the values of its arguments every time the function is called

def greet(name,greeting="namaste"):
    print(f"{greeting},{name}")
greet("Binod",greeting="gurubaa darsan")