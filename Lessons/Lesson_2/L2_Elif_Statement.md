# Elif Statement  

Sometimes we may wish to use an alternative test should our previous test evaluate as ``False``. 

``elif`` which is short for else if, lets us do exactly that.

## 1. Using the Elif Statement

We can test another condition after the first condition as follows:

### 1.1 Example - if ... elif 

```python
# change these to experiment with the if..elif block
x = 4
y = 5

if x < y:
  # block of code
  print("x is less than y")
elif x > y:
  # block of code
  print("x is greater than y")

```

Here depending on the values of ``x`` and ``y`` one (and only one) of the ``print`` statements is executed. 

If ``x`` is less than ``y`` then ``x < y`` is ``True`` and the first block is executed. 

If ``x`` is greater than ``y`` then ``x < y`` is ``False`` and the ``elif`` part is checked. As ``x > y`` is ``True``, the second block is executed. 

What about if ``x`` and ``y`` are equal?

Copy the code above into **main.py** and experiment with different values of `x` and `y`.

### 1.2 Example - if ... elif ..else

We can also include an ``else`` statement, now our program will output when ``x`` and ``y`` are equal.

```python
# change these to experiment with the if..elif..else block
x = 4
y = 5

if x < y:
  # block of code
  print("x is less than y")
elif x > y:
  # block of code
  print("x is greater than y")
else:
  # block of code
  print("x is equal to y")
```

You should think about this and realise that there are three possibilities. 

1. ``x`` is less than ``y``
2. ``x`` is greater than ``y``
3. ``x`` is equal to ``y``

If the first two are ``False``, then it must be that ``x`` is equal to ``y``. We don't need a test, we can just the ``else`` statement.


### 1.3 Example - multiple elif statements

Another example is testing to see if the first letter of someone's name begins with a vowel.

```python
input_name = input("Please enter your name:\n")

# convert the name to lowercase
name = input_name.lower()

if name[0] == "a":
  print("The name begins with an a")
elif name[0] == "e":
  print("The name begins with an e")
elif name[0] == "i":
  print("The name begins with an i")
elif name[0] == "o":
  print("The name begins with an o")
elif name[0] == "u":
  print("The name begins with an u")
else:
  print("The name does not begin with a vowel")

```

I suggest trying each of these programs out in **main.py**.

***Note that this is not the most efficient way to do this, we can either use the newer match statement available since Python 3.10 (version). We could also do a similar thing using lists***

***
# === TASK ===
Write a program that outputs whether a number is positive, negative, or zero. Your program should accept numbers of type ``float``.

* If the number is positive it should output ``Your number is positive!``
* If the number is negative it should output ``Your number is negative!``
* If the number is zero it should output ``Your number is zero!``
&nbsp;

For example, your program should output the following given these inputs:
```
Please enter a number:
2.3
Your number is positive!
```

```
Please enter a number:
-3.3
Your number is negative!
```

```
Please enter a number:
0
Your number is zero!
```
***Note that to pass the tests you must have exactly the output above, apart from the numbers which will differ depending on what the user inputs.***
***