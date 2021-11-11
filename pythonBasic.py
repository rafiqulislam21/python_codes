print("hello world")
#this is a comment
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

x = "awesome"
print("Python is " + x)


x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
#global
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)