#Types of Operators
print('\n---Types of Operator---\n')

#Arithmetic Operators
print(''' Arithmetic Operators
* (+) Addition
* (-) Subtraction
* (*) Multiplication
* (/) Division => 5/2 = 2.5
* (%) Modulus  => 5%2 = 1  (remainder value)
* (**) Exponent => 5**2 = 25
* (//) Floor Division => 5//2 = 2 (quotient value)''')

#Comparison(Relational) Operators
print('''\nComparison(Relational) Operators\n
- compare the values on either side and decide the relation
* (==) Equal
* (!=) Not Equal
* (>) Greater than
* (<) Less than
* (>=) Greater than or equal
* (<=) Less than or equal \n''')

#Examples for Relational Operators
a = 5
b = 10
print('if a = 5 and b = 10, ')
if (a == b):
    print('Line 1: a is equal to b')
else:
    print('Line 1: a is not equal to b')

if (a != b):
    print('Line 2: a is not equal to b')
else:
    print('Line 2: a is equal to b')

if (a > b):
    print('Line 3: a is greater than b')
else:
    print('Line 3: a is not greater than b')

if (a < b):
    print('Line 4: a is less than b')
else:
    print('Line 4: a is not less than b')

if (a <= b):
    print('Line 5: a is either less than or equal to b')
else:
    print('Line 5: a is neither less than nor equal to b')

if (a >= a):
    print('Line 6: a is either greater than or equal to b')
else:
    print('Line 6: a is neither greater than nor equal to b')

#Assignment Operators
print('''\n---Assignment Operators---\n
* (=)   Assignment Op =>  c = 100 assigns 100 into c
* (+=)  Add AND => c += a is equivalent to c = c + a
* (-=)  subtract AND => c -= a is equivalent to c = c - a
* (*=)  Multiply AND => c *= a is equivalent to c = c * a
* (/=)  Divide AND => c /= a is equivalent to c = c / a
* (%=)  Modulus AND => c %= a is equivalent to c = c % a
* (**=)  Exponent AND => c **= a is equivalent to c = c ** a
* (//=)  add AND => c //= a is equivalent to c = c // a \n''')

#Examples for Assignment Operators

a = 5
c = 100
print('\n if a = 5, c = 100, ')
c += a
print('c += a: Value of c is ', c)

a = 5
c = 100
print('\n if a = 5, c = 100, ')
c -= a
print('c -= a: Value of c is ', c)

a = 5
c = 100
print('\n if a = 5, c = 100, ')
c *= a
print('c *= a: Value of c is ', c)

a = 5
c = 100
print('\n if a = 5, c = 100, ')
c /= a
print('c /= a: Value of c is ', c)

a = 5
c = 100
print('\n if a = 5, c = 100, ')
c %= a
print('c %= a: Value of c is ', c,'<= remainder value')

a = 5
c = 100
print('\n if a = 5, c = 100, ')
c //= a
print('c //= a: Value of c is ', c, '<= quotient value')

#Bitwise Operators
print('''\n---Bitwise Operators---\n
- work on bits and perform bit-by-bit operation
* (&) Binary AND
* (|) Binary OR
* (^) Binary XOR
* (~) Binary Ones Complement
* (<<) Binary Left Shift
* (>>) Binary Right Shift\n''')

#Examples for Bitwise Operators
a = 150
b = 300
print('a = ', a, 'Binary value of a = ', bin(a))
print('b = ', b, 'Binary value of b = ', bin(b))

x = 0
x = a & b
print('\nResult of AND is ', x, '\nBinary value is ', bin(x))

y = 0
y = a | b
print('\nResult of OR is ', y, '\nBinary value is ', bin(y))

z = 0
z = a ^ b
print('\nResult of XOR is ', z, '\nBinary value is ', bin(z))

c = ~a
print('\nResult of COMPLEMENT is ', c, '\nBinary value is ', bin(c))

c = a << 3
print('\nResult of LEFT SHIFT is ', c, '\nBinary value is ', bin(c))

c = a >> 3
print('\nResult of RIGHT SHIFT is ', c, '\nBinary value is ', bin(c))

#Python Logical Operators
print('''\n---Python Logical Operators---\n
- Assume x is true and y is false
* (and) Logical AND => (x and y) is false
* (or) Logical OR => (x or y) is true.
* (not) Logical NOT => Not(x and y) is true.''')

#Python Membership Operators
print('''\n---Python Membership Operators\n
- test for membership in a sequence, such as strings, lists, or tuples
* in => x in y
* not in => x not in y\n''')

a = 3
b = 7
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]

if (a in list1):
    print('a is available in list1')
else:
    print(' a is not available in list1')

if (a in list2):
    print('a is available in list2')
else:
    print('a is not available in list2')

if (b in list1):
    print('b is available in list1')
else:
    print('b is not available in list1')

if (b in list2):
    print('a is available in list2')
else:
    print(' a is not available in list2')

#Python Identity Operators
print('''\n---Python Identity Operators\n
- compare the memory locations of two objects
* is => x is y
* is not => x is not y\n''')

x = 5
y = 5
print('x = ', x, ':', id(x), 'y = ', y, ':', id(y))

if(x is y): #same result code => if(id(x) == id(y)):
    print('x and y have the same identity\n')
else:
    print('x and y do not have the same identity\n')

a = 10
b = 20
print('a = ', a, ':', id(a), 'b = ', b, ':', id(b))

if(a is not b):
    print('a and b do not have the same identity\n')
else:
    print('a and b  have the same identity\n')

