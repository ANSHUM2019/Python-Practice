# Python-Practice
[Python Compiler](https://www.onlinegdb.com/online_python_compiler)
| [Python Automation](https://automatetheboringstuff.com/chapter1/)
| [python Learn](http://www.pythonlearn.com/html-007/index.html)
| [Hello World](https://github.com/ANSHUM2019/Python-Practice/blob/master/HelloWorld.py)

# Importing a Module
import math
from math import factorial

## Providing alias to Module
import math as M
e.g, M.factorial(5)

from math import factorial as fact
e.g, fact(5)

finding no. of digits in the factorial
len(str(fact(5)))

# Scalar types and Fundamentals
## int
* decimal, binary, octal, hexadecimal numbers are supported
e.g, 10, 0b10, 0o10, 0x10 , int("1000", 3)
Casting of values to integer is allowed in python.
e.g, int("10"), int(-3.6)
*Note: int(inf) throws error*
## float
eg, 3.125, 1.6e-35
Python automatically wiches while displaying the no.
any operation betn int and float is promoted to Float

##None
x = None
x is None # returns true

## bool
0,length of 0 are considered as false.
bool(0) #False
bool(0.2) #True

Relational Operator
==,!=, <, >, >=, <=

Conditional Statements
if bool("eggs"):
and
if "eggs":
are equivalent

if
elif
else

# while statement
while True:
    response = input()
	if int(response) % 7 == 0:
	    break
# operators
* 

