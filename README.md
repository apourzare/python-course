# Section 03

## Loop

### While

```python
count = 1
while count <= 5:
  print("Count is:", count)
  count += 1
# Output: 1, 2, 3, 4, 5
```

### For

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print("Fruit:", fruit)
# Output: apple, banana, cherry
```

--------

## Helper Function in Loop

### Range

```python
for i in range(5):
  print("Number:", i)
# Output: 0, 1, 2, 3, 4
```

### Range Between two number

```python
for i in range(2, 6):
  print("Number:", i)
# Output: 2, 3, 4, 5
```

### Range Between two number with Stepper

```python
for i in range(1, 10, 2):
  print("Odd number:", i)
# Output: 1, 3, 5, 7, 9
```

--------

## Work with Lists

### Declare List

```python
names = ["Amin", "Sara", "Ali"]
print(names)
```

### Add to List

```python
names = ["Amin", "Sara", "Ali"]
names.append("Reza")
print(names)  # Output: ["Amin", "Sara", "Ali", "Reza"]

```

### Get an Item from List

```python
names = ["Amin", "Sara", "Ali"]
print(names[0])  # Output: Amin
print(names[-1])  # Output: Reza
```

### Remove an Item from List

```python
names = ["Amin", "Sara", "Ali", "Reza"]
names.remove("Sara")
print(names)  # Output: ["Amin", "Ali", "Reza"]
```

------------

## Exercises

- Write a program that prints numbers from 1 to 10.
- Write a program that prints each item in a list of strings in reverse order.
- Use a `for` loop to calculate the sum of numbers from 1 to 20.