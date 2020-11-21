print('\n--- Strings ---\n')
print('''--- Updating Strings
- update an existing string by reassigning a variable to another string\n''')

str1 = 'Hello'
print('Original String: ', str1)
print('Updating String: ', str1[:6] + ' Python')

print('\n--- Most Common Use Escape Character ---\n')
print(r'\t => tab : ' + 'This is \t tab')   #\t => tab
print(r'\n => new line: ' + 'This is  \n new line')     #\n => new line

print('\n--- String Special Operators ---\n')
special_operators = [
 '+\t => concatenation',
 '*\t => repetition',
 '[]\t => slice',
 '[:]\t => range slice',
 'r\R\t => raw string',
 '%\t => string formatting']

for s_o in special_operators:
    print(s_o)
str1 = 'Hello'
str2 = 'Python'
print('str1 + str2: ', str1 + str2)
print('str1*2 and str2*4: ', str1*2, str2*4)
print('str1[0] and str2[0]: ', str1[0], str2[0])
print('str1[0:4] and str2[4:6]: ', str1[0: 4], str2[4: 6])
print('Raw String: ', r'C:\\blah blah')
print('Item name is %s and price is %d$ ! ' %('Zara Chino', 79))

print('\n--- String Formatting Operators ---\n')
formatting_operators = [
    '%c => character',
    '%s => string conversion',
    '%i => signed decimal integer',
    '%d => signed decimal integer',
    '%u => unsigned decimal integer',
    '%o => octal integer',
    '%x => hexadecimal integer(lowercase letters)',
    '%X => hexadecimal integer(UPPERcase letters)',
    '%e => exponential notation (with lowercase e)',
    '%E => exponential notation (with UPPERcase E)',
    '%f => floating point real number',
    '%g => the shorter of %f and %e',
    '%G => the shorter of %f and %E'
]

for f_o in formatting_operators:
    print(f_o)

print('\n--- Unicode String --- \n')
print('---Built-in String Methods---')
built_in_string_method = [
    '1: capitalize()',
    '2: center(width, fillchar)',
    '3: count(str, beg=0, end=len(string))',
   r'4: decode(encoding="UTF-8",errors ="strict")',
   r'5: encode(encoding="UTF-8",errors ="strict")',
    '6: endswith(suffix, beg=0, end=len(string)',
    '7: expandtabs(tabsize=8)',
    '8: find(str, beg=0, end=len(string))',
    '9: index(str, beg=0, end=len(string))',
    '10: isalnum()',
    '11: isalpha()',
    '12: isdigit()',
    '13: islower()',
    '14: isnumeric()',
    '15: isspace()',
    '16: istitle()',
    '17: isupper()',
    '18: join(seq)',
    '19: len(string)',
    '20: ljust(width, fillchar)',
    '21: lower()',
    '22: lstrip()',
    '23: maketrans()',
    '24: max(str)',
    '25: min(str)',
    '26: replace(old, new, max)',
    '27: rfind(str, beg=0, end=len(string))',
    '28: rindex(str, beg=0, end=len(string))',
    '29: rjust(width, fillchar)',
    '30: rstrip()',
    '31: split(str="",num = string.count(str))',
    r"32: splitlines(num= string.count('\n'))",
    '33: startswith(str, beg=0, end=len(string))',
    '34: strip([chars])',
    '35: swapcase()',
    '36: title()',
    '37: translate(table, deletechars="")',
    '38: upper()',
    '39: zfill(width)',
    '40: isdecimal()'
]

for b_in_s in built_in_string_method:
    print(b_in_s)

#String capitalize() Method
print('''\n--- String capitalize() Method ---
- return first character capitalize''')

cap_str = 'i love python programming!'
print('Original String: ', cap_str)
print('str.capitalize(): ', cap_str.capitalize())

#String center() Method
print('''\n--- String center() Method ---
center(width, fillchar)
- return centered in a string of length width
- padding is done using the specified fillchar
- default filler is space
- width => total width of the string
- fillchar => filler character''')

center_str = 'i love python programming!'
print('Original String: ', center_str)
print("str.center(40, '*'): ", center_str.center(40, '*'))




