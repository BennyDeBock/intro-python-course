# Concepts

- Conditional Statements (if, elif, else).
- Loops (for and while).
- Loop Control (break, continue, pass).

## Conditional statements

As with many things, life is complex. Code can also be complex.
Sometimes we want to write code that only executes when certain conditions are met. We call these conditional statements. You can see this as a sort of flowchart.

Here's an example in pseudocode:
```
BEGIN
  Input A is 5

  IF A is bigger than 3 THEN
    PRINT "A is bigger than 3"
  ELSE IF A is equal to 3 THEN
    PRINT "A is equal to 3"
  ELSE
    PRINT "A is smaller than 3"

  IF A is equal to 5 THEN
    PRINT "A is equal to 5"
  ELSE
    PRINT "A is not equal to 5"
END
```

To translate the above pseudocode into actual python code, we have to make use of a few keywords.

The keywords introduced in this chapter are:
- `if`: Checks a condition and executes the code underneath if the expression results to True
- `elif`: Checks a condition as before, but has to come after an if statement. 
- `else`: Takes no condition, but has to come after an if statement. This is meant as an alternate path

The end of the expression is always followed by a colon (`:`)

The above pseudocode would translate to the following in python:

```py
A = 5

# Because we checked for equality and bigger than, we can assume A is smaller than 3. Thus we don't need to write an expression
if A > 3:
  print('A is bigger than 3')
elif A == 3:
  print("A is equal to 3")
else
  print("A is smaller than 3")

if A == 5:
  print("A is equal to 5")
else
  print("A is not equal to 5")

```
## Loops (for and while).



### Loop Control (break, continue, pass).