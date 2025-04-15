# Concepts

- Basic Operations (addition, subtraction, multiplication, division).
- Comments and Documentation.

## Variables and Data types
### Data Types
Python gives us a few default data types we can use. An example of a string is the following line from the previous example:
```py
"Hello world! My name is <insert your name>"
```

Below is a summary of a few basic data types. Collections will be touched upon in chapter 5.

| Data Type | Example | Category | Description |
|---|---|---|---|
| str | "this is text" | Text | A collection of characters that makes up words/sentences |
| int | 3 | Numeric | Whole numbers. Defaults to 0 |
| float | 3.14 | Numeric | Decimal numbers. Defaults to 0.0 |
| bool | True | Boolean | A True or False value |

### Expressions
Expressions are lines of code that execute an operation. Usually these operations can return a result. These results can then be assigned to a variable for further processing.

Some examples of an expression:
```py
1 + 1 # Returns 2

# The print function is a default given by python
# It expects some type of input, and then prints it to the console
print("Hello world")
```

### Variables
Now that we know some of the data types as well as what an expression is, we want some way to store information. We can do this by using variables.

To use variables, these should get a name. This name is allowed to exist out of a combination of letters, numbers and underscores. These are also case sensitive.

> **Note:** You can't use any name reserved by python syntax. These are things like 'if', 'not', 'while', etc...

To create and assign these variables, we use the `=` operator.

Examples of correct variable names:
```py
name = "John"
_age = 34
Email = "a@b.be"
Email2 = "b@b.be"

# The following are all variations but valid names. Note that these are 3 different variables
firstName = "John"
first_name = "John"
FirstName = "John"
```

Examples of incorrect variable names:
```py
# Variable names should not contain whitespaces
first Name = "John"

# Variables can't contain special characters
em@il = "a@b.be"
dollars$ = 500

# Variables names cannot start with a number
2Email = "b@b.be"
```

Tips: 
- Use meaningful variable names
- Use naming conventions: [A handy guide](https://pythonguides.com/python-naming-conventions/)
  - You can make your own conventions, just make sure to stick to it for clarity

## Basic Operations

Python offers us a few basic operators to use. 

### Arithmic operators
These operators are used for mathematical calculations like addition, substraction, multiplication, etc. Most of these are the same as those used in everyday mathematics.

| Operator | Description | Example | Result |
|---|---|---|---|
| + | Addition | 5 + 8 | 13 |
| - | Substraction | 5 - 8 | -3 |
| * | Multiplication | 9 * 7 | 63 |
| / | Division | 5 / 2 | 2.5 |
| // | Floor Division | 5 / 2 | 2 |
| % | Modulo(Remainder) | 69 / 10 | 9 |
| ** | Exponentation(Power) | 4 ** 3 | 64 |

### Assignment operators
These operators are used for assigning values to variables. The can also be used to perform arithmetic operations in combination with assignments.

| Operator | Description | Example | Equivalent operation |
|---|---|---|---|
| = | Assign a value to a variable | x = 2 | N/A |
| += | Add and assign | x += 5 | x = x + 5 |
| -= | Subtract and assign | x -= 5 | x = x - 5 |
| *= | Multiply and assign | x *= 5 | x = x * 5 |
| /= | Divide and assign | x /= 5 | x = x / 5 |
| //= | Floor divide and assign | x //= 5 | x = x // 5 |
| %= | Modulo and assign | x %= 5 | x = x % 5 |
| **= | Exponentiate and assign | x **= 5 | x = x ** 5 |

### Comparison Operators
These operators are used to compare two values. The result of this comparison returns a Boolean value (`True` or `False`)

| Operator | Description | Example | Result |
|---|---|---|---|
| == | Equal to | 4 == 4 | True |
| != | Not equal to | 4 != 5 | True |
| > | Greater than | 3 > 5 | False |
| < | Lesser than | 3 < 5 | True |
| >= | Greater than or equal | 6 >= 6 | True |
| <= | Lesser than or equal | 7 <= 4 | False |

### Logical Operators
These operators are used to combine and manipulate Boolean values. For the following examples, we'll assume `x = 10`

| Operator | Description | Example | Evaluates to | Result |
|---|---|---|---|---|
| and | Returns True if all boolean values are True; Otherwise returns False | (x > 2) and (x < 20) | (True) and (True) | True |
| or | Returns True if at least one boolean values is True; Otherwise returns False | (x > 11) or (x < 11) | (False) and (True) | True |
| not | Returns True if all boolean values are True; Otherwise returns False | not(x == 10) | not(True) | False |

> **Note:** It's important to note that the or operation stops from the moment it encounters a True value. Hence the order of your expressions may matter


> **Note 2:** If you are checking to see if a number is between two numbers, you can use the following syntax. `0 < x < 100`



## Comments

While clean code practices make a codebase much clearer, sometimes it's necessary to add additional comments to be able to fully understand what something does. 

Comments always come after the `#` operator. This signifies that a comment will be written after this symbol.

**However!** Sometimes we want to write comments over multiple lines. For this we use `"""` as this denotes a multiline comment

Examples:
```py
# This calculation adds up to 2
1+1

2+3 # Adds up to 5

# The code below is commented out, meaning it won't print 2 to the console
# print(2)
print(5)

"""
This is a multiline comment
Here i can freely press enter
and this will still count as one comment
"""


# This is another multiline comment
# But here i need a comment indicator
# every time i want to create a new line


```

# Exercises
[Exercise: Variables and datatypes](./exercises/variablesAndDataTypes.py)  
[Exercise: Basic operations](./exercises/basicOperations.py)  
[Exercise: Comments and Documentation](./exercises/commentsAndDocumentation.py)

# Congratulations

Now that we know how to create variables and how expressions work, there's loads we can do. Follow the next chapter [Basics of python syntax](../02-Basics-of-python-syntax/02%20-%20Basics%20of%20python%20syntax.md) to continue your journey!