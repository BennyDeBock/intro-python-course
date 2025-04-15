# Concepts

- Variables and Data Types (int, float, str, bool).
- Basic Operations (addition, subtraction, multiplication, division).
- Comments and Documentation.

## Data types
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

## Expressions
Expressions are lines of code that execute an operation. Usually these operations can return a result. These results can then be assigned to a variable for further processing.

Some examples of an expression:
```py
1 + 1 # Returns 2

# The print function is a default given by python
# It expects some type of input, and then prints it to the console
print("Hello world")
```

## Variables
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


# Congratulations

Now that we know how to create variables and how expressions work, there's loads we can do. Follow the next chapter [Basics of python syntax](../02-Basics-of-python-syntax/02%20-%20Basics%20of%20python%20syntax.md) to continue your journey!