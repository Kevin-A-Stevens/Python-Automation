## Data Types
# int = Whole numbers without fractions
# float = Real numbers. Numbers that have a fraction
# string = Between "" or ''
# None empty or returns nothing

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

## Creating our own functions - def function_name(function_parameter):
def greeting(name, department):
    print("Welcome, " + name)  # function body
    print("You are part of " + department)

greeting("Kevin", "Python Developer")

## Returning values
base = 6
height = 3
area = (base*height)/2

# keyword return = tells pythpn this is the return value of the function
def area_triangle(base, height):
    return base*height/2

area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b
print("The sum of both area is: " + str(sum))

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)

# len function - calculates length of a string
name = "Kevin"
number = len(name) * 9

print("Hello " + name + ". Your lucky number is " + str(number))

def lucky_number(name):
    number = len(name) * 9
    print("Hello " + name + ". Your lucky number is " + str(number))

lucky_number("Kevin")

def hint_username(username):
    if len(username) < 3:
        print("Username cannot be less than 3 characters")
    elif len(username) > 15:
        print("Username cannot be at most 15 characters")
    else:
        print("valid username")

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False



