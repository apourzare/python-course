# Section 01

---

## Basic

---

### Get Python Version

```
python --version
```

### Run Python Script

```
python {filename}.py
```

### Get Python Version with Script File

> make main.py file

```
import sys

print(sys.version)
```

#### Run

```
python main.py
```

### Use Comment

1. Single Line

```
# This is comment
```

2. Multi Line

```
"""
This is 
multi line 
comment
"""
```

***

## Creating Variables

---

### Declare

```
x = 7
name = "Amin"
pi = 3.14
fruits = ["apple", "banana"]
```

### Casting

```
x = str(3)       # x = '3'
y = int('3')     # y = 3
z = float(3)     # z = 3.0
```

### Get the Type

```angular2html
x = 7
y = "Amin"

print(type(x))
print(type(y)) 
```

### Case-Sensitive

```angular2html
a = 7
A = "Amin"

# A will not overwrite a
# a = 7
# A = "Amin"
```

### Variable Name Rules

- A variable name must start with a letter or the underscore characters
- A variable name cannot start with a number
- A variable nam can only contain alpha-numeric characters and underscores (A-z, 0-9, and _)
- Variable names are case-sensitive (age, Age, AGE, aGe are many different variables)

### Multi Words Variable Names

1. Camel Case

```
studentName = "Amin"
```

2. Pascal Case

```
StudentName = "Amin"
```

3. Snake Case

```
student_name = "Amin"
```

### Many Values to Multiple Variables

```angular2html
x, y, z = 7, "Amin", 3.14

print(x)      # 7
print(y)      # Amin
print(z)      # 3.14
```

### Unpack a Collection

```angular2html
fruits = ["apple", "banana"]
x, y = fruits

print(x)         # apple
print(y)         # banana
```

---

# Section 02

---

## Globals Variable