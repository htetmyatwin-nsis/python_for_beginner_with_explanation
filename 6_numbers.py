import math
import random

print('''\n---Numbers---\n
* (int) 
=> positive or negative whole numbers with no decimal point, unlimited size
* (float) 
=> decimal point including scientific notation, with E or e indicating the power of 10
=> 7.7e3 = 7.7 x 10^3 = 7700
* (complex) 
=> a + bJ where a and b are floats and J(or j) represent the square root of -1 (imaginary number)
=> the real part of the number is a, the imaginary part is b
''')

#Number Type Conversion
print('''\n---Number type conversion---\n
* int(x) => convert x to a plain integer
* long(x) => convert x to a long integer
* float(x) => convert x to a floating-point number
* complex(x) => convert x to a complex number with real part x and imaginary part zero
* complex (x,y) => convert x and y to a complex number with real part x and imaginary part y
                => x and y are numeric expressions''')

#Mathematical Functions
print('\n---Mathematical Functions---\n')

print('''---Number abs() Method---
- abs(x) => absolute value of x, positive distance between x and zero\n''')

print('abs(-10) : ', abs(-10))
print('abs(10.37): ', abs(10.37))

print('''\n---Number fabs() Method---
- fabs(x) 
=> absolute value of x, similar to the abs() functions but differences
=> - abs() is a built in function whereas fabs() is defined in math module
=> - fabs() function works only on float and integer whereas abs() works with complex number also\n''')

#fabs() requires to import math function
print('math.fabs(-10.37): ', math.fabs(-10.37))
print('math.fabs(10.37): ', math.fabs(10.37))
print('math.fabs(10.73): ', math.fabs(10.73))
print('math.fabs(math.pi): ', math.fabs(math.pi))

print('''\n---Number exp() Method---
exp(x) => exponential of x: e^x\n''')

#exp() requires to import math function
print('math.exp(-10.37): ', math.exp(-10.37))
print('math.exp(10.37): ', math.exp(10.37))
print('math.exp(10.73): ', math.exp(10.73))
print('math.exp(math.pi): ', math.exp(math.pi))

print('''\n---Number ceil() Method---
ceil(x) => the ceiling value of x, smallest integer not less than x\n''')

#ceil() requires to import math function
print('math.ceil(-10.37): ', math.ceil(-10.37))
print('math.ceil(10.37): ', math.ceil(10.37))
print('math.ceil(10.73): ', math.ceil(10.73))
print('math.ceil(math.pi): ', math.ceil(math.pi))

print('''\n---Number floor() Method---
floor(x) => the floor value of x, largest integer not greater than x\n''')

#floor() requires to import math function
print('math.floor(-10.37): ', math.floor(-10.37))
print('math.floor(10.37): ', math.floor(10.37))
print('math.floor(10.73): ', math.floor(10.73))
print('math.floor(math.pi): ', math.floor(math.pi))

print('''\n---Number log() Method---
log(x) => the natural logarithm of x, for x>0\n''')

#log() requires to import math function
print('math.log(10.37): ', math.log(10.37))
print('math.log(10.73): ', math.log(10.73))
print('math.log(math.pi): ', math.log(math.pi))

print('''\n---Number log10() Method---
log10(x) => base-10 logarithm of x for x>0\n''')

#log10() requires to import math function
print('math.log10(10.37): ', math.log10(10.37))
print('math.log10(10.73): ', math.log10(10.73))
print('math.log10(math.pi): ', math.log10(math.pi))

print('''\n---Number max() Method---
max(x, y, z, ...) => the largest of its arguments\n''')

print('max(80, 100, 1000): ', max(80, 100, 1000))
print('max(-20, -30, -40): ', max(-20, -30, -40))
print('max(-1, 0, -2): ', max(-1, 0, -2))

print('''\n---Number min() Method---
min(x, y, z, ...) => the smallest of its arguments\n''')

print('min(80, 100, 1000): ', min(80, 100, 1000))
print('min(-20, -30, -40): ', min(-20, -30, -40))
print('min(-1, 0, -2): ', min(-1, 0, -2))

print('''\n---Number modf() Method---
modf(x) => the fractional and integer parts of x in two-item tuple
        => both parts have the same sign as x
        => integer part is returned as a float\n''')

#modf() requires to import math function
print('math.modf(-10.37): ', math.modf(-10.37))
print('math.modf(10): ', math.modf(10))
print('math.modf(10.73): ', math.modf(10.73))
print('math.modf(math.pi): ', math.modf(math.pi))

print('''\n---Number pow() Method---
pow(x, y) => return the value of x^y \n''')

#pow() requires to import math function
print('math.pow(10, 3): ', math.pow(10, 3))
print('math.pow(10, -3): ', math.pow(10, -3))
print('math.pow(10, 0): ', math.pow(10, 0))
print('math.pow(math.pi, 3): ', math.pow(math.pi, 3))


print('''\n---Number round() Method---
round(x, n) => built-in function, return x rounded to n digits from the decimal point
            => x - numeric expression
            => n - number of digits from decimal point up, default is 0\n''')

print('round(10.37): ', round(10.37))
print('round(12.345, 1): ', round(12.345, 1))
print('round(10.0001, 2): ', round(10.0001, 2))
print('round(-100.11156, 3): ', round(-100.11156, 3))

print('''\n---Number sqrt() Method---
sqrt() => return the square root of x for x > 0\n''')

#sqrt() requires to import math function
print('math.sqrt(100): ', math.sqrt(100))
print('math.sqrt(7): ', math.sqrt(7))
print('math.sqrt(math.pi): ', math.sqrt(math.pi))

#Ramdom Number Functions
print('''\n---Random Number Functions---
- used for games, simulations, testing, security and privacy applications
- following functions that are commonly used\n''')

print('''---Number choice() Method---
- return a random item from a list, tuple or string
- not accessible directly, need to import random module\n''')

print('return a random number from range(50): ', random.choice(range(50)))
print('return random element from list[1, 2, 3, 4, 5, 6, 7]: ', random.choice([1, 2, 3, 4, 5, 6, 7]))
print('return random character from "Python": ', random.choice('Python'))

print('''\n---Number randrange() Method---
- return a randomly selected element from range(start, stop, step)
- not accessible directly, need to import random module
  * start - start point of the range, default => 0
  * stop - stop point of the range
  * step - value with which number is incremented, default => 1\n''')

print('randrange(1, 10, 1): ', random.randrange(1, 10, 1))
print('randrange(1, 100, 2): ', random.randrange(1, 100, 2))
print('randrange(1, 9999, 3): ', random.randrange(1, 9999, 3))
print('randrange(100): ', random.randrange(100))

print('''\n---Number random() Method---
- return a random floating point number in the range [0.0 to 1.0]
- not accessible directly, need to import random module\n''')

print('first random() number: ', random.random())
print('second random() number: ', random.random())
print('third random() number: ', random.random())

print('''\n---Number seed() Method---
- initialize the basic random number generator
- call this function before calling any other random module function
- not return any value\n''')

random.seed()
print('random number with seed ', random.random())

print('''\n---Number shuffle() Method---
- randomizes the items of a list in place
- not accessible directly, need to import shuffle module\n''')

list = [1, 2, 3, 4, 5]
print('Original List: ', list)
random.shuffle(list)
print('First Reshuffled List: ', list)
random.shuffle(list)
print('Second Reshuffled List: ', list)

print('''\n---Number uniform() Method---
- return a random float
- not accessible directly, need to import uniform module\n''')

print('Random Float uniform(10, 100): ', random.uniform(10, 100))
print('Random Float uniform(9, 999): ', random.uniform(9, 999))

print('\n--- Trigonometric Functions ---\n')
trigo_list = ['acos(x) : return the arc cosine of x, in radians',
              'asin(x) : retunn the arc sin of x, in radians',
              'atan(x) : return the arc tangent of x, in radians',
              'atan2(y, x) : return atan(y/x), in radians',
              'sin(x) : return the sin of x radians',
              'cos(x) : return the cosine of x radians',
              'tan(x) : return the tangent of x radians',
              'hypot(x, y) : return the Euclidean norm, sqrt(x*x + y*y)',
              'degree(x) : convert angle x from radians to degrees',
              'radians(x) : convert angle x from degrees to radians']
for trigolist in trigo_list:
    print(trigolist, '\n')

print('''--- Number acos() Method ---
acos(x) => return the arc cosine of x, in radians
        => x in the range -1 to 1
        => if x > 1, it will generate 'math domain error'\n''')

print('acos(-1): ', math.acos(-1))
print('acos(0): ', math.acos(0))
print('acos(1): ', math.acos(1))
print('acos(0.25): ', math.acos(0.25))

print('''\n--- Number asin() Method ---
asin(x) => return the arc sine of x, in radians
        => x in the range -1 to 1
        => if x > 1, it will generate 'math domain error'\n''')

print('asin(-1): ', math.asin(-1))
print('asin(0): ', math.asin(0))
print('asin(1): ', math.asin(1))
print('asin(0.25): ', math.asin(0.25))

print('''\n--- Number atan() Method ---
atan(x) => return the arc tangent of x, in radians
        => x must be a numeric value\n''')

print('atan(-1): ', math.atan(-1))
print('atan(0): ', math.atan(0))
print('atan(1): ', math.atan(1))
print('atan(0.25): ', math.atan(0.25))
print('atan(-10): ', math.atan(-10))
print('atan(10): ', math.atan(10))

print('''\n--- Number atan2() Method ---
atan2(y, x) => return the atan(y/x), in radians
        => x and y - numeric value\n''')

print('atan2(-1, -1): ', math.atan2(-1, -1))
print('atan2(10, 10): ', math.atan2(10, 10))
print('atan2(5, -1): ', math.atan2(5, -1))
print('atan2(0, 0): ', math.atan2(0, 0))
print('atan2(-1, 0): ', math.atan2(-1, 0))
print('atan2(0, -1): ', math.atan2(0, -1))

print('''\n--- Number sin() Method ---
sin(x) => return the sine of x radians
       => x must be a numeric value
       => return value between -1 and 1 \n''')

print('sin(5): ', math.sin(5))
print('sin(-5): ', math.sin(-5))
print('sin(0): ', math.sin(0))
print('sin(2*math.pi): ', math.sin(2*math.pi))

print('''\n--- Number cos() Method ---
cos(x) => return the cosine of x radians
       => x must be a numeric value
       => return value between -1 and 1\n''')

print('cos(5): ', math.cos(5))
print('cos(-5): ', math.cos(-5))
print('cos(0): ', math.cos(0))
print('cos(2*math.pi): ', math.cos(2*math.pi))

print('''\n--- Number tan() Method ---
tan(x) => return the tangent of x radians
       => x must be a numeric value
       => return value between -1 and 1\n''')

print('tan(5): ', math.tan(5))
print('tan(-5): ', math.tan(-5))
print('tan(0): ', math.tan(0))
print('tan(math.pi/2): ', math.tan(math.pi/2))

print('''\n--- Number hypot() Method ---
hypot(x, y) => return the Euclidean norm, sqrt(x*x, y*y)
            => x and y must be a numeric value
            => returns Euclidean norm, sqrt(x*x + y*y)\n''')

print('hypot(3, 4): ', math.hypot(3, 4))
print('hypot(5, 12): ', math.hypot(5, 12))
print('hypot(-3, 4): ', math.hypot(-3, 4))
print('hypot(0, 4): ', math.hypot(0, 4))
print('hypot(7, -4): ', math.hypot(7, -4))

print('''\n--- Number degrees() Method ---
degrees(x) => convert angle x from radians to degrees
           => x must be a numeric value
           => return the degree value of an angle\n''')

print('degrees(5): ', math.degrees(5))
print('degrees(-5): ', math.degrees(-5))
print('degrees(0): ', math.degrees(0))
print('degrees(math.pi): ', math.degrees(math.pi))
print('degrees(math.pi/2): ', math.degrees(math.pi/2))
print('degrees(math.pi/4): ', math.degrees(math.pi/4))
print('degrees(2*math.pi): ', math.degrees(2*math.pi))

print('''\n--- Number radians() Method ---
radians(x) => convert angle x from degrees to radians
           => x must be a numeric value
           => return the radian value of an angle\n''')

print('radians(5): ', math.radians(5))
print('radians(-5): ', math.radians(-5))
print('radians(0): ', math.radians(0))
print('radians(math.pi): ', math.radians(math.pi))
print('radians(math.pi/2): ', math.radians(math.pi/2))
print('radians(math.pi/4): ', math.radians(math.pi/4))
print('radians(2*math.pi): ', math.radians(2*math.pi))

print('\n--- Mathematical Constants ---\n')
print('The mathematical constant pi: ', math.pi)
print('The mathematical constant e: ', math.e)