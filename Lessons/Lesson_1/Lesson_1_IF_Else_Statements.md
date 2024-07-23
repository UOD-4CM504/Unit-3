# If ... Else Statement  

  As stated in the overview of this unit. A **conditional**  statement has three parts:

1. Boolean test - an expression that evaluates to **True** or **False**
2. **True** block - a block of code that is executed if the test evaluates to **True**
3. **False** block - a block of code that is executed if the test evaluates to **False**


## 1. Structure of a conditional statement

In Python, a **conditional** ``if`` statement has the following form:
  
  ```python
if <boolean expression>:
    # If the boolean expression is True, run this block of code
else:
    # If the boolean expression is False, run this block of code
    
  
  ```
You can see how this mirrors the diagram from the overview of this unit, if the boolean expression is ``True``, execute the ``True`` block, else it is ``False``, execute the ``False`` block.

![Conditional flow diagram](assets/unit3_overview_branching.png)

### Example 1.1 - Just an if statement

The following example tests if a variable ``x`` is less than``5`` and only prints out if ``x`` is less than ``5``

```python
print("code before if statement")

# store 4 in the variable x
x = 4

# Test the variable using the boolean expression x < 5?
if x < 5:
    print(f"{x} is less than 5")
  
print("code after if statement")
```

The whole output of the program is as follows:

```
code before if statement
4 is less than 5
code after if statement
```

If we change ``x = 10`` then the program will not execute the statement ``print(f"{x} is less than 5")`` and the output will be:

```
code before if statement
code after if statement
```

Copy and paste the following program into main.py and experiment by entering different numbers.

```python
# get some input from the user and store as an int
input_string = input("Please enter a whole number\n")
x = int(input_string)

print("code before if statement")

if x < 5:
    print(f"{x} is less than 5")
  
print("code after if statement")
```

### Example 1.2 - if ... else statement

The following example tests if a variable ``x`` is less than ``5`` and prints out information for both cases.

```python
print("code before if statement")

# Test the variable using the boolean expression x < 5?
if x < 5:
    print(f"{x} is less than 5")
else:
    print(f"{x} is greater than or equal to 5")
  
print("code after if statement")
```

In this example ``x = 7`` which is greater than ``5``, therefore ``x < 5`` evaluates to ``False`` and the program prints ``7 is greater than or equal to 5`` (the ``else`` block)

The whole output of the program is as follows:

```
code before if statement
7 is greater than or equal to 5
code after if statement
```

Try copying the code below into **main.py** and running the program. Think about the following:

1. What happens with different ``int`` values of ``x``?
2. What happens if ``x`` is not an ``int``, for example of type ``str``?

```python
# get some input from the user and store as an int
input_string = input("Please enter a whole number\n")
x = int(input_string)

print("code before if statement")

# Test using the boolean expression x < 5?
if x < 5:
    # run this code if boolean expression is True
    print(f"{x} is less than 5")
else:
    # run this code if boolean expression is False
    print(f"{x} is greater than or equal to 5")
  
print("code after if statement")
```

## 2. Indentation

You will notice that the code is indented, this is how Python determines **blocks** of code. Indentation is determined by the programmer, I would stick to 2 or 4 spaces. Repl.it defaults to 2 spaces.

It can be done using a different number of spaces or the tab character, but you should be consistent in your program. Try the code without the indentation. What happens?

### Example 2.1 - No indentation
  ```python
print("code before if statement")

x = 4

if x < 5:
print(f"{x} is less than 5")
else:
print(f"{x} is greater than or equal to 5")
  
print("code after if statement")
  ```

You will see that you get the following error - ``IndentationError: expected an indented block``. 

## 3. Compound Boolean Expressions

The conditional test for the ``if`` statement can be a more complicated expression as long as it evaluates to ``True`` or ``False``. 

For example, the following program tests to see if a number is between 1 and 10:

### Example 3.1 - Logical And
  ```python
# get some input from the user and store as an int
x = int(input("Enter a whole number:\n"))

if (x > 0) and (x < 11):
    print("Number is between 1 and 10")
else:
    print("Number is not between 1 and 10")
```
Here the boolean expression (test) is ``(x > 0) and (x < 11)`` which requires that both ``(x > 0)`` and ``(x < 11)`` need to be ``True`` for the whole expression to be ``True``.

### Example 3.2 - Logical Not
  ```python
# ask the user for a number and cast it to an int
x = int(input("Enter a whole number:\n"))

if not x < 10 :
    print("Number is above 10")

```
Here the boolean expression (test) is ``not x < 0``. This will first evaluate ``x < 0`` and then take a ``not`` of the result. e.g. if ``x = 11`` then ``x < 10`` is ``False``, therefore ``not x < 10`` is ``True``. 

Try out these programs in **main.py** and make sure you understand what they do.

***
# === TASK ===
You can test if a number is ***even*** or ***odd*** using the modulus operator ``%``.

For example, ``4 % 2 = 0`` evaluates to ``0`` because ``2`` divides ``4`` with no remainder.

However, `` 7 % 2 = 1`` evaluates to ``1`` because ``2`` divides ``7`` with remainder ``1``.

We can use this to evaluate if a number is ***odd*** or ***even***. The expression ``x % 2 == 0`` evaluates to ``True`` if ``x`` is ***even*** and ``False`` if it is ***odd***.

The expression ``x % 2 == 0`` compares the left side ``x % 2`` to the right side ``0`` to see if they are equal.

For example,
 
| ``x`` | ``x % 2`` | ``x % 2 == 0`` |
| --- | --- | --- |
| ``4`` | ``0`` | ``True`` |
| ``7`` | ``1`` | ``False`` |

I suggest you try some even and odd examples out in the console if you don't understand this.

E.g. Try:

```python
# test 4 to see if it is even
4 % 2 == 0  # will print out True as 4 % 2 evaluates to 0
```

```python
# test 7 to see if it is even
7 % 2 == 0  # will print out False as 7 % 2 evaluates to 1
```

Write a program that asks a user for a number and then prints out whether it is ***even*** or ***odd***.

Your program should work as follows:
```
Please enter a whole number:
7
Your number is odd!
```

```
Please enter a whole number:
4
Your number is even!
```
***Note that to pass the tests you must have exactly the output above, apart from the numbers which will differ depending on what the user inputs.***
***