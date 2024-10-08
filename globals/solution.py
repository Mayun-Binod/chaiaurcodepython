y='have global keyboard'

def glob():
    print (f"hello python {y}")
glob()


x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


# 

def myfunc():
  global z
  z = "fantastic"

myfunc()

print("Python is " + z)