# Nested if Statements  

It is possible to nest if statements within other if statements. This can be useful for testing multiple conditions but allowing us to run code for each conditional.

## 1. Nested if Statement

We can nest if statements as follows:

### 1.1 Example - Nested if Statement
```python
x = 101

if x > 100:
  print("Above 100, ", end="")
  if x > 150:
    print("and also above 150!")
  else:
    print("but not above 150!")
```

As ``x = 101`` the first program will first execute the statement ``print("Above 100, ", end="")`` and then execute the statement ``print("but not above 150!")``. Try different values of x by pasting the code above into **main.py**.

If we compare this with:

```python
x = 101

if (x > 100) and (x > 150):
  print("Above 100, and also above 150!")
```

The second program cannot do this and only prints out ``"Above 100, and also above 150!`` if ``x`` is greater than ``150``. 

If ``x = 99`` or ``x = 130`` the program will print nothing. 

You should make sure you understand the program flow. The two program flows are depicted in the diagram below.

![Nested if statement flow](assets/nested_if_flow.png)

## 2. Indentation

You should note that in the example given in 1.1, the blocks of code are given by indentation. If we just examine the structure of the example it looks as follows:

```python
# main block of code, anything aligned with this is in this block
if x > 100:
  # True block of code
  print("Above ten,")
  if x > 150:
    # True block of code
    print("and also above 150!")
  else:
    # False block of code
    print("but not above 150!")
```

This is also illustrated by the diagram below. You should note that the indentation defines each of the blocks of code.

![Nested if statement flow with blocks](assets/nested_if_flow_blocks.png)
  
# === TASK ===
Using **nested if statements**, write a program that asks the user for a whole number. Your program should do the following:
* If the number is divisible by 3 and 5 it should print out

``Your number is divisible by 3 and 5.``
* If the number is divisible by 3 and **NOT** 5 it should print out
 
``Your number is divisible by 3 and NOT 5.``
* If the number is **NOT** divisible by and by 5 it should print out
 
``Your number is NOT divisible by 3 and is divisible by 5.``
* If the number is **NOT** divisible by and by **NOT** 5 it should print out
 
``Your number is NOT divisible by 3 and 5.``

Your program should match the examples below. I have given examples for each output.

```
Please enter a number:
15
Your number is divisible by 3 and 5.
```

```
Please enter a number:
12
Your number is divisible by 3 and NOT 5.
```

```
Please enter a number:
20
Your number is NOT divisible by 3 and is divisible by 5.
```

```
Please enter a number:
22
Your number is NOT divisible by 3 and 5.
```

**HINT: We learned how you can test if a number is divisible by 2 in the Lesson: If ... Else Statement earlier in this unit.**
***
***Note that to pass the tests you must have exactly the output above, apart from the numbers which will differ depending on what the user inputs.***
