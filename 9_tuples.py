#Python 3 - Tuples
print('''\n--- Python 3: Tuples ---
- a sequence of immutable python objects
- comma-separated values (items) between parentheses\n''')

tup1 = ('Python', 'C#', 'Kotlin', 'Vue')
tup2 = (1, 2, 3, 100, 10000)
tup3 = 'a', 'e', 'i', 'o', 'u'
print('tup1 | tup2 | tup3: ', tup1, ' | ', tup2, ' | ', tup3)

#Accessing Values in Tuples
print('''\n--- Accessing Values in Tuples ---
- use square brackets for slicing along with the index
- indices to obtain the value available at that index\n''')

tup = ('FrontEnd', 2020, 'BackEnd', 'Database', 2022, 'Cloud')
print('Original Tuple: ', tup)
print('After using tup[0]: ', tup[0])
print('After using tup[3]: ', tup[3])
print('After using tup[2:]: ', tup[2:])
print('After using tup[0:2]: ', tup[0:2])

#Updating Tuples
print('''\n--- Updating Tuples ---
- tuples are immutable i.e cannot update or change the value of tuple elements
- indices to obtain the value available at that index\n''')

tup1 = ('Maths', 'Chemistry', 'Physics')
tup2 = ('Biology', 'Economics')

#tuples immutable: cannot update
#tup1[3] = 'Biology'

#concatenation
tup3 = tup1 + tup2
print('Original tuples: ', tup1, ' | ', tup2)
print('After concatenation: ', tup3)

#Delete Tuple Elements
#Basic Tuples Operations
#Indexing, Slicing and Matrixes
#No Enclosing Delimiters
#Built-in Tuple Functions
#Tuple len() Method
#Tuple max() Method
#Tuple min() Method
#Tuple tuple() Method
