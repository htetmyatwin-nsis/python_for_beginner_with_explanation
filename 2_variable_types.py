#Variable Types
print('\n---Variable Types---\n')
print('''- Variables are nothing but reserved memory locations to store values
- When your create a variable, you reserve some space in the memory\n''')

#Standard Data Types
print('---Standard Data Types---\n')
print(''' Python has five standard data types-
* Numbers
* String
* List
* Tuple
*Dictionary\n''')

#Three Different Numerical Types
print('''---Three Different Numerical Types---
* int (signed integers)
* float (floating point real values
* complex (complex number)''')

int_value = [10, 100, -789, -0x260, 0x69]
float_value = [0.0, 15.20, -21.9, -32.54e100, 70.2e12]
complex_value = [3.14j, 45.j, 9.322e36j, .89j, -.6545+0j, 3e+26J]

print('\nIntegers Value')
for iv in int_value:
    print(iv)


print('\nFloat Value')
for fv in float_value:
    print(fv)


print('\nComplex Value')
for cv in complex_value:
    print(cv)

#Python Strings
print('\n---Python Strings---\n')
print('''- Subsets of strings can be taken using the slice operator ([] and [:]) with index starting at 0 in the beginning of the string
- The plus (+) sign is the string concatenation operator and the asterisk (*) is the repetition operator''')
str = 'Are you a pyton programmer? '
print(str)      # Print complete string
print(str[0])   # Print first character of the string
print(str[2:7]) # Print characters starting from 3rd to 7th
print(str[2:])  # Print string starting from 3rd character
print(str*2)    # Print string two times
print(str + "\nYes, I'm a python programmer.") # Prints concatenated string

#Python Lists
print('\n---Python Lists---\n')
print('''- Most versatile of python's compound data types
- Items separated by commas(,) and enclosed within square brackets ([])
- Similar to arrays in C
- Elements and size of list can be changed\n''')

list1 =['abcd', 'dog', 'cat', 123, 12.3]
list2 = ['efgh', 'bird', 'tree', 325j, 12e78]

print(list1)        # Print complete list1
print(list2)        # Print complete list2
print(list1[0])     # Print first element of the list1
print(list2[3])     # Print 4th element of the list2
print(list1 + list2) # Print concatenated lists

#Python Tuples
print('\n---Python Tuples---\n')
print('''- Another sequence data type that is similar to the list
- Unlike list, tuples are enclosed within parenthesis()
- Tuples cannot be updated => read-only\n''')

tuple1 = ('xyz', 'butterfly', 'bee', 23J, 11e11, 70.2)
tuple2 = ('pqr', 'mouse', 223, 'Rocky')
print(tuple1)           # Print complete tuple1
print(tuple2)           # Print complete tuple2
print(tuple1[2:4])      # Print elements starting from 3rd till 4th
print(tuple2 * 3)       # Print tuple2 three times
print(tuple1 + tuple2)  # Print concatenated tuples

#Python Dictionary
print('\n---Python Dictionary---\n')
print('''- kind of hash-table type
- consist of key-value pairs
- key can be almost any python type => usually numbers ro strings
- values, on the other hand, any arbitrary python object => {1:"Hello")
- dictionaries are enclosed by curly braces ({ })
- values can be assigned and accessed using square braces ([ ])\n''')

dict1 = {}
dict1 ['one'] = 'This is 1'
dict1 [2] = 'This is two'
dict2 = {'name': 'Charlie', 'age': 2, 'duty': 'guard'}

print(dict1['one'])         # Print value for 'one' key
print(dict1[2])             # Print value for 2 key
print(dict2)                # Print complete dict2
print(dict2.keys())         # Print all the keys of dict2
print(dict2.values())       # Print all the values of dict2
print(dict2['age'])         # Print value for 'age' key