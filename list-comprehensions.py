# List Comprehension Syntax Breakdown

# The basic syntax of a list comprehension is:
# [expression for item in iterable]

# Let's break down each component:

# 1. The expression: This is what you want to do with each item
# 2. The item: This is the variable that represents each element in the iterable
# 3. The iterable: This is the collection you're looping through (like a list, range, etc.)

# Let's visualize this with a simple example:

# Traditional for loop:
numbers = []
for i in range(1, 6):  # i is the item, range(1, 6) is the iterable
    numbers.append(i)  # i is the expression (in this case, unchanged)
print("Traditional loop result:", numbers)

# List comprehension:
# [expression for item in iterable]
numbers_lc = [i for i in range(1, 6)]
#            │  │    │     │
#            │  │    │     └── The iterable (range of numbers)
#            │  │    └──────── The keyword 'in' (part of the syntax)
#            │  └───────────── The item variable (represents each element)
#            └──────────────── The expression (what to do with each item)
print("List comprehension result:", numbers_lc)

# Let's see a more complex example with transformation:
# Traditional for loop:
squares = []
for i in range(1, 6):
    squares.append(i ** 2)  # i ** 2 is the expression (squaring the number)
print("Traditional loop squares:", squares)

# List comprehension:
# [expression for item in iterable]
squares_lc = [i ** 2 for i in range(1, 6)]
#             │      │    │     │
#             │      │    │     └── The iterable
#             │      │    └──────── The keyword 'in'
#             │      └───────────── The item variable
#             └──────────────────── The expression (squaring the item)
print("List comprehension squares:", squares_lc)

# Adding conditions (filtering):
# The syntax with a condition is:
# [expression for item in iterable if condition]

# Traditional for loop with condition:
even_numbers = []
for i in range(1, 11):
    if i % 2 == 0:  # This is the condition
        even_numbers.append(i)
print("Traditional loop even numbers:", even_numbers)

# List comprehension with condition:
# [expression for item in iterable if condition]
even_numbers_lc = [i for i in range(1, 11) if i % 2 == 0]
#                  │  │    │     │          │     │
#                  │  │    │     │          │     └── The condition
#                  │  │    │     │          └──────── The keyword 'if'
#                  │  │    │     └─────────────────── The iterable
#                  │  │    └───────────────────────── The keyword 'in'
#                  │  └──────────────────────────────── The item variable
#                  └─────────────────────────────────── The expression
print("List comprehension even numbers:", even_numbers_lc)

# You can also use more complex expressions:
# Let's create a list of the first 5 powers of 2
powers_of_two = [2 ** i for i in range(5)]
print("Powers of 2:", powers_of_two)  # [1, 2, 4, 8, 16]

# You can use string methods too:
words = ["hello", "world", "python"]
capitalized = [word.capitalize() for word in words]
print("Capitalized words:", capitalized)  # ['Hello', 'World', 'Python']

# You can even use list comprehensions with nested loops:
# Traditional nested loops:
pairs = []
for x in range(1, 3):
    for y in range(1, 3):
        pairs.append((x, y))
print("Traditional nested loops:", pairs)  # [(1, 1), (1, 2), (2, 1), (2, 2)]

# List comprehension with nested loops:
pairs_lc = [(x, y) for x in range(1, 3) for y in range(1, 3)]
print("List comprehension nested loops:", pairs_lc)  # [(1, 1), (1, 2), (2, 1), (2, 2)]
