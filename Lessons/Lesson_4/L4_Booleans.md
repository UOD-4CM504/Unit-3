# Booleans  

  This lesson introduces you to the built-in data type ``bool``. Booleans are essential in computer science and take on either a value of ``True`` or ``False``. 

``True`` and ``False`` are keywords in Python and are used to represent their respective boolean values. You can assign them to variables, for example:

```python
my_bool = True
type(my_bool)
```

The above code assigns the value ``True`` to ``my_bool`` and then checks the type. Try this in the console and you will see that ``my_bool`` is now an object of type ``<class 'bool'>``.

## 1. Boolean Expressions

You can compare two objects of the same type using the comparison operators listed in the table below. These expressions will return either ``True`` or ``False`` and are known as boolean expressions.

### 1.1 Comparison Operators

| Operator | Name | Example |
| --- | --- | --- | 
| ``==`` | Equal |	``x == y`` |
| ``!=`` | Not equal |``x != y`` |
| ``>`` |	Greater than | ``x > y`` |
|``<`` | Less than | ``x < y`` |
| ``>=`` | Greater than or equal to | ``x >= y`` |
| ``<=`` | Less than or equal to | ``x <= y`` |

### 1.2 Comparing Numbers

For example, the following expressions compare ``int`` objects and evaluate to:

| Expression | Result | 
| --- | --- | 
| ``3 < 5`` | ``True`` |
| ``3 > 3`` | ``False`` |
| ``6 >= 6`` | ``True`` |
| ``3 == 5`` | ``False`` |
| ``3 != 5`` | ``True`` |

### 1.3 Comparing Strings

Interestingly you can also compare other objects such as ``str``. The following,

```python
"held" < "helm"
```
evaluates to ``True`` and,

```python
"help" < "helm"
```
evaluates to ``False``. 

Python knows how to compare the order of strings! It looks at each character in turn and compares their order in the alphabet. Try experimenting. For example, what do the following two expressions return?

```python
"hel" < "helm"
```

```python
"hello" < "helm"
```

Try to reason about the answers that you get.

### 1.4 Comparing Booleans

Believe it or not, you can also compare the order of Booleans. 

```python
True < False      # (Evaluates to False)
```

```python
False < True      # (Evaluates to True)
```

This is because Python also represents ``True`` as the bit value ``1`` and ``False`` as the bit value ``0``. Now the above should make sense!

### 1.5 Comparing Different Types
Do you know how to order the ``str`` ``"hello"`` and the ``int`` ``10``? I don't and neither does Python.

```python
"hello" < 10     
```
results in the following exception:

```
TypeError: '<' not supported between instances of 'str' and 'int'
```
Two objects you can mix are numbers (``int`` and ``float``),

```python
4 < 5.6       # (Evaluates to True)
```
and numbers and booleans (``bool``),

```python
4 < True      # (Evaluates to False)
```
because ``True`` is also represented by ``1``. 

## 2. Logical Operators

Boolean expressions can be combined with logical operators to create larger boolean expressions:

| Operator | Description | Example |
| --- | --- | --- | 
| ``and`` | Returns ``True`` if both statements are ``True``	| ``x < 5 and  x < 10`` |
| ``or`` | Returns ``True`` if one of the statements is ``True``	| ``x < 5 or  x < 10`` |
| ``not`` | Reverse the result, returns ``False`` if the result is ``True`` | ``not(x < 5 and x < 10)``

### 2.1 Order of Precedence and Left-to-Right

All the logical operators given above have lower precedence than the arithmetic operators and comparison operators.

You will also notice that the order of precedence (high to low) for the logical operators is ``not``, ``and`` and then ``or``. This means you evaluate ``not`` first, then ``and``, then ``or``. 

You also evaluate left-to-right.

| Operator | Name |
| --- | --- |
| ``()`` | Parentheses | 
| ``**`` | Exponentiation | 
| ``*``, ``/``, ``%``, ``//`` | Multiplication, Division, Modulus, Floor Division | 
| ``+``, ``-`` | Addition, Subtraction |
| ``==``, ``!=``, ``<``, ``>``, ``<=``, ``>=`` | Comparison Operators |
| ``not``	| Logical NOT |
| ``and`` |	Logical AND |
| ``or`` |	Logical OR |

### 2.1 Evaluating a Complicated Boolean Expression
The table gives quite a complicated expression for the ``not`` example. 

```python
not(x < 5 and x < 10) 
```

Let's look at this for ``x = 4``,

```
# This is not code, we are manually evaluating to see how Python works with this expression

not(x < 5 and x < 10)     # (Substitute x = 4)
not(4 < 5 and 4 < 10)     # (Evaluate 4 < 5)
not(True and 4 < 10)      # (Evaluate 4 < 10)
not(True and True)        # (Evaluate True and True)
not(True)                 # (Evaluate not True)
False 
```

and for ``x = 6``,


```
# This is not code, we are manually evaluating to see how Python works with this expression

not(x < 5 and x < 10)     # (Substitute x = 4)
not(6 < 5 and 6 < 10)     # (Evaluate 6 < 5)
not(False and 6 < 10)      # (Evaluate False and ....)
not(False)                 # (Evaluate not False)
True 
```
``False and 6 < 10`` evaluated to ``False`` because ``and`` requires both expressions to be ``True``. As the first is ``False``, why bother evaluating the second?

This is known as short-circuit evaluation or McCarthy evaluation. Named after the great John McCarthy.

### 2.2 Truth Tables

We can consider the result of combining two ``bool`` variables ``p`` and ``q``. The following are known as truth tables and display the result for different combinations of ``p`` and ``q`` using ``and`` and ``or``.

#### 2.2.1 Truth Table for  ``and``
| ``p`` | ``q`` | ``p and q`` |
| --- | --- | --- | 
| ``True`` | ``True`` | ``True`` |
| ``True`` | ``False`` | ``False`` |
| ``False`` | ``True`` | ``False`` |
| ``False`` | ``False`` | ``False`` |

#### 2.2.2 Truth Table for  ``or``

| ``p`` | ``q`` | ``p or q`` |
| --- | --- | --- | 
| ``True`` | ``True`` | ``True`` |
| ``True`` | ``False`` | ``True`` |
| ``False`` | ``True`` | ``True`` |
| ``False`` | ``False`` | ``False`` |

***
# === TASK ===

For this program you should fix the single line instructed. You should also just run the tests directly to see if it works

Copy the following code into **main.py**.

```python
# DO NOT TOUCH THESE LINES. THEY ARE USED BY THE TESTS
# If you want to test this program, when you hit Run, enter values of True or False via the console
is_raining = bool(int(input()))
no_hat = bool(int(input()))
#######################################################

# You should fix this line to by forming an expression using is_raining and no_hat to produce the correct result for takes_umbrella. 

# e.g takes_umbrella = is_raining or no_hat

# Note you only have to fix this line to pass the tests. No if statements etc.. required!

takes_umbrella = True

print(takes_umbrella)
```
 
Sam doesn't like getting his hair wet and sometimes wears a hat.

* On days that it is raining and Sam is not wearing a hat, Sam takes his umbrella.
* On days that it is raining and Sam is wearing a hat, Sam does not take an umbrella.
* If it is not raining Sam does not take an umbrella.
&nbsp;

We use two variables ``is_raining`` and ``no_hat`` to represent whether it is raining and if Sam is wearing a hat.

* If it is raining ``is_raining = True``
* If Sam is **NOT** wearing a hat ``no_hat = True``.
&nbsp;

Using a third variable ``takes_umbrella`` determine if Sam should take his umbrella by combining ``is_raining`` and ``no_hat``.
 
For example, on days that it is raining and Sam is not wearing a hat the variables will have the following values:
* ``is_raining = True``
* ``no_hat = True``
* ``takes_umbrella = True``
&nbsp;

``is_raining`` and ``no_hat`` have been set up for you in **main.py**. Combine them with logical operators to get the correct value of ``takes_umbrella``.

HINT: You should consider the truth table and fill in the missing entries. This will then give you a hint to what the expression should be.

| `is_raining` | `no_hat`| `takes_umbrella` |
| :--: | :--: | :--: |
| `False` | `False` | ?|
| `False` | `True` |?|
| `True` | `False` |?|
| `True` | `True` | `True`|
***

[W3Schools - Python Booleans](https://www.w3schools.com/python/python_booleans.asp)

[W3Schools - Python Comparison Operators](https://www.w3schools.com/python/python_operators.asp)