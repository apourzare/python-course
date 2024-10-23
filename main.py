import sys

print(sys.version)

# This is Comment


"""
This is 
multi line 
comment
"""

"""
Create variables
---
Declare
"""
x = 7
name = "Amin"
pi = 3.14
fruits = ["apple", "orange", "pear"]

# Casting
a = str(3)
b = int("3")
c = float(3)

print(a)
print(b)
print(c)

# Get the Type
print(type(a))
print(type(b))
print(type(c))

# Case-Sensitive
d = 7
D = "Amin"

# Multi Words Variable Names

studentName = "Ali"
StudentName = "Hassan"
student_name = "Milad"

# Many Values to Multiple Variables
e, f, g = 2.17, "Mino", 10.98

print("e is: ", e)
print("f is: ", f)
print("g is: ", g)

# Unpack a Collection
# fruits = ["apple", "orange", "pear"]
h, i, j = fruits
print("h is: ", h)
print("i is: ", i)
print("j is: ", j)
