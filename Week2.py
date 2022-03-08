## Data Types
# int = Whole numbers without fractions
# float = Real numbers. Numbers that have a fraction
# string = Between "" or ''

# print function
print(7+8)
print("Hello " + "World")

# Type function
print(type("a"))
print(type(2))
print(type(2.5))

# TypeError = incompatible data types such as 2 + "3"

## Variables = containers for data

length = 10
width = 2
area = length * width
print(area)

# Implicit conversion = interpreter converts one data type to another
# In this example, 7 is converted to a float to make both data types the same
print(7 + 8.5)
print("a" + "b" + "c")

# Explicit conversion and str function
# In this example we use the str function to convert the number to a string
base = 6
height = 3
area = (base*height)/2
print("The area of the triangle is: " + str(area))



