import base64

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
   r'4: decode(encoding="UTF-8",errors ="strict") | encode(encoding="UTF-8",errors ="strict")',
    '5: startswith(str, beg=0, end=len(string)) | endswith(suffix, beg=0, end=len(string)',
    '6: expandtabs(tabsize=8)',
    '7: find(str, beg=0, end=len(string)) | index(str, beg=0, end=len(string))',
    '8: isalnum() | isalpha()',
    '9: isdigit() | isnumeric() | isdecimal()',
    '10: islower() | isupper()',
    '11: upper() | lower()',
    '12: isspace()',
    '13: istitle() | title()',
    '14: max(str) | min(str)',
    '15: ljust(width, fillchar) | rjust(width, fillchar)',
    '16: strip([chars])| lstrip() | rstrip()',
    '17: join(seq)',
    '18: len(string)',
    '19: maketrans() | translate(table, deletechars="")',
    '20: replace(old, new, max)',
    '21: rfind(str, beg=0, end=len(string))',
    '22: rindex(str, beg=0, end=len(string))',
    '23: split(str="",num = string.count(str))',
    r"24: splitlines(num= string.count('\n'))",
    '25: swapcase()',
    '26: zfill(width)'
]

for b_in_s in built_in_string_method:
    print(b_in_s)

#String capitalize() Method
print('''\n--- String capitalize() Method ---
capitalize() - return first character capitalize''')

cap_str = 'i love python programming!'
print('Original String: ', cap_str)
print('str.capitalize(): ', cap_str.capitalize())

#String center() Method
print('''\n--- String center() Method ---
center(width, fillchar) - return centered in a string of length width
                        - padding is done using the specified fillchar
                        - default filler is space
                        - width => total width of the string
                        - fillchar => filler character\n''')

center_str = 'i love python programming!'
print('Original String: ', center_str)
print("str.center(40, '*'): ", center_str.center(40, '*'))

#String count() Method
print('''\n--- String count() Method ---
count() - return the number of occurrences of substring sub in th range\n''')

count_str =  'Are you a python programmer?'
sub1 = 'A'
print('count_str.count("A"): ', count_str.count(sub1))
sub2 = 'a'
print('count_str.count("a"): ', count_str.count(sub2))
sub3 = '?'
print('count_str.count("?"): ', count_str.count(sub3))
sub4 = ' '
print('count_str.count("space"): ', count_str.count(sub4))

#String decode()/encode() Method
print('''\n--- String decode()/enccode() Method --
decode()/encode() - decode/encode the string using the codec registered for encoding\n''')

decode_str =  'Are you a python programmer?'
encode_str = decode_str.encode('utf-16', 'strict')

print('Original Decoded string: ', decode_str)
print('Encode String (UTF-16): ', encode_str)

#need to import base64
decode_str = base64.b64encode(decode_str.encode('utf-8', errors='strict'))
print('Encoded string (base64): ', decode_str)

#String startswith()/ endswith() Method
print('''\n--- String startswith()/ endswith() Method ---
startswith() - check whether the string starts with specific prefix
endswith() - return True if the string ends with the specific suffix, otherwise return false\n''')

#startswith() method
print('-- Printing startswith() method --')
startswith_str = 'Are you a python programmer?'
prefix = 'Are'
print('Original String: ', startswith_str)
print('start with Are: ', startswith_str.startswith(prefix))
print('start with Are with start value 10: ', startswith_str.startswith(prefix, 10))
prefix = 'python'
print('start with python: ', startswith_str.startswith(prefix))
print('start with python with start and end value: ', startswith_str.startswith(prefix, 0, 20))

#endswith() method
print('\n-- Printing endswith() method --')
endswith_str = 'Are you a python programmer?'
suffix = '?'
print('Original String: ', endswith_str)
print('end with ?: ', endswith_str.endswith(suffix))
print('end with ? with start value 40: ', endswith_str.endswith(suffix, 40))
suffix = 'python'
print('end with python: ', endswith_str.endswith(suffix))
print('end with python with start and end value: ', endswith_str.endswith(suffix, 0, 20))


#String expandtabs() Method
print('''\n--- String expandtabs() Method --
expandtabs() - return a copy of the string in which the tab characters 
             - optionally using the given tabsize (default 8)\n''')

expandtabs_str = 'Are you \ta python programmer?'
print('Original String: ', expandtabs_str)
print('Default expanded tab string: ', expandtabs_str.expandtabs()) #default tabsize 8
print('User expanded tab string: ', expandtabs_str.expandtabs(24))

#String find()/index() Method
print('''\n--- String find()/index() Method --
find()/ index() - determine and search the specific string or substring 
                - find() not found =>  return -1
                - index() not found => return "substring not found error\n''')

str1 = 'Are you a python programmer?'
str2 = 'py'
str3 = '?'

#find() method
print('-- Printing find() method, not found return -1 --')
print('Find "py" :', str1.find(str2))
print('Find "?" : ', str1.find(str3))
print('Find "py" with index 30 :', str1.find(str2, 30))
print('Find "?" with index 50 : ', str1.find(str3, 50))

#index() method
print('\n-- Printing index() method, not found return "substring not found error --')
print('index "py" :', str1.index(str2))
print('index "?" : ', str1.index(str3))
# print('index "py" with number 30 :', str1.index(str2, 30))
# print('index "?" with number 50 : ', str1.index(str3, 50))

#String isalnum()/isalpha() Method
print('''\n--- String isalnum()/isalpha Method --
isalnum() - check whether the string consists of alphanumeric characters
isalpha() - check whether the string consists of alphabetic characters only
          - both return True/False\n''')

#isalnum() method
print('-- Printing isalnum() --')
isalnum_str1 = 'python3' #no space in this string
isalnum_str2 = 'python version'
print('python3: ', isalnum_str1.isalnum())
print('python version: ', isalnum_str2.isalnum())

#isalpha() method
print('\n-- Printing isalpha() --')
isalpha_str1 = 'python' #no space & digit
isalpha_str2 = 'python3'
isalpha_str3 = 'python version'
print('pyton: ', isalpha_str1.isalpha())
print('python3: ', isalpha_str2.isalpha())
print('pyton version: ', isalpha_str3.isalpha())

#String isdigit()/ isdecimal()/isnumeric() Method
print('''\n--- String isdigit()/isdecimal Method --
isdigit() - check whether the string consists of digits only
isdecimal() - check whether the string consists of only decimal characters
isnumeric() - checks whether the string consists of only numeric charaters
          - all return True/False\n''')

#isdigit() method
print('-- Printing isdigit() --')
isdigit_str1 = '369'
isdigit_str2 = 'python 3.9'
isdigit_str3 = 'python version'
isdigit_str4 = '3.9'
print('369: ', isdigit_str1.isdigit())
print('python 3.7: ', isdigit_str2.isdigit())
print('python version: ', isdigit_str3.isdigit())
print('3.9: ', isdigit_str4.isdigit())

#isdecimal() method
print('\n-- Print isdecimal() --')
isdecimal_str1 = 'python 3.9'
isdecimal_str2 = '3.9'
isdecimal_str3 = '39'
print('python 3.9: ', isdecimal_str1.isdecimal())
print('3.9: ', isdecimal_str2.isdecimal())
print('39: ', isdecimal_str3.isdecimal())

#isnumeric() method
print('\n-- Printing isnumeric() --')
isnumeric_str1 = 'python 3.9'
isnumeric_str2 = '39'
print('python 3.9: ', isnumeric_str1.isnumeric())
print('39: ', isnumeric_str2.isnumeric())

print('''\n--- String isupper()/islower() Method ---
isupper() - check whether all the case-based characters(letters) of the string are uppercase
islower() - check whether all the case-based character(letters) of the string are lowercase
          - return True/False\n''')

str1 = 'python'
str2 = 'Python'
str3 = 'PYTHON'
#isupper() method
print('python.isupper(): ', str1.isupper(),
      '\nPython.isupper(): ', str2.isupper(),
      '\nPYTHON.isupper(): ', str3.isupper())

#islower() method
print('\npython.islower(): ', str1.islower(),
      '\nPython.islower(): ', str2.islower(),
      '\nPYTHON.islower(): ', str3.islower())

print('''\n--- String upper()/lower() Method ---
upper() - return a copy of string to uppercase
lower() - return a copy of string to lowercase\n''')

str_to_upper = 'are you a python programmer?'
str_to_lower = 'ARE YOU A PYTHON PROGRAMMER?'
print('original string: ', str_to_upper, '\tString to uppercase: ', str_to_upper.upper())
print('original string: ', str_to_lower, '\tString to lowercase: ', str_to_lower.lower())

#sting title() method
print('''\n--- String title() method ---
title() - return a copy of the string in which first characters of all the words are capitalzied\n''')

sample_str = 'this is title! are u serious?'
print('title() testing: ', sample_str.title())

#string istitle() method
print('''\n--- String istitle() method ---
istitle() - check whether all the string in title format
          - return True/False\n''')

title_str1 = 'Are You A Python Programmer?'
title_str2 = 'are you a python programmer?'
title_str3 = 'ARE YOU A PYTHON PROGRAMMER?'

print('istitle() testing: Are You A Python Programmer?', title_str1.istitle())
print('istitle() testing: are you a python programmer?', title_str2.istitle())
print('istitle() testing: ARE YOU A PYTHON PROGRAMMER?', title_str3.istitle())

#string isspacce() method
print('''\n--- String isspace() method ---
isspace() - check whether the string consists of whitespace
          - return True/False\n''')

space_str1 = '    '
space_str2 = 'are you a python programmer?'
print('isspace() testing: (    )', space_str1.isspace())
print('isspace() testing: are you a python programmer?', space_str2.isspace())

#strign max()/ min() method
print('''\n--- Stirng max()/ min() method ---
max() - return the max alphabetical character from the string
min() - return the min alphabetical character from the string\n''')

eg_str = 'Are you a python programmer?'
eg_str1 = 'www.python.org/xyz'
print('max() testing: ', max(eg_str))
print('max() testing: ', max(eg_str1))
print('min() testing: ', min(eg_str))
print('min() testing: ', min(eg_str1))

#String ljust() method
print('''\n--- String ljust() Method ---
ljust() - return the string left justified in a string of length width
        - padding is done using the specified fillchar (default is a space)
        - fillchar must be exactly one character long, otherwise => error returns\n''')

ljust_string = 'Are you a python programmer?'
print('Original String: ', ljust_string)
print('After left justified: ', ljust_string.ljust(40, '?'))
print('After left justified: ', ljust_string.ljust(60, '*'))

#String rjust() method
print('''\n--- String rjust() Method ---
rjust() - return the string right justified in a string of length width
        - padding is done using the specified fillchar (default is a space)
        - fillchar must be exactly one character long, otherwise => error returns\n''')

rjust_string = 'Are you a python programmer?'
print('Original String: ', rjust_string)
print('After right justified: ', rjust_string.rjust(40, '/'))
print('After right justified: ', rjust_string.rjust(60, '|'))

#String strip() method
print('''\n--- String strip() Method ---
strip() - return a copy of the string in which all chars have been stripped from the beginning and end of the string\n''')

strip_str = '***Backend Development: Python, Golang, Nodejs, Java, C#.Net***'
print('Original String: ', strip_str)
print('After "*" stripped: ', strip_str.strip('*'))

#String lstrip() method
print('''\n--- String lstrip() Method ---
lstrip() - return a copy of the string in which all chars have been stripped from the beginning of the string\n''')

lstrip_str = '||||||Are you a serious python programmer?||||||'
print('Original String: ', lstrip_str)
print('After "|" left stripped: ', lstrip_str.lstrip('|'))
lstrip_str1 = '***** Frontend | Backend *****'
print('Original String: ', lstrip_str1)
print('After "*" left stripped: ', lstrip_str1.lstrip('*'))

#String rstrip() method
print('''\n--- String rstrip() Method ---
rstrip() - return a copy of the string in which all chars have been stripped from the end of the string\n''')

rstrip_str = '//////Are you a serious python programmer?//////'
print('Original String: ', rstrip_str)
print('After "/" right stripped: ', rstrip_str.rstrip('/'))
rstrip_str1 = '***** Frontend | Backend *****'
print('Original String: ', rstrip_str1)
print('After "*" right stripped: ', rstrip_str1.rstrip('*'))

#String join() method
print('''\n--- String join() Method ---
join(seq_str) - return a string in which the string elements of sequence have been joined by other string separator\n''')

join_string1 = '_'
join_string2 = ' | '
sequence_string1 = ('x', 'y', 'z')
sequence_string2 = ('a', 'b', 'c')
print(join_string1.join(sequence_string1))
print(join_string2.join(sequence_string2))

#String len() method
print('''\n--- String len() Method ---
len() - return the length of the string\n''')
len_str = 'Are you a python programmer?'
len_str1 = 'The quick brown fox jumps over the lazy dog.'
print('"Are you a python programmer?" : string length =>', len(len_str))
print('"The quick brown fox jumps over the lazy dog." : string length =>', len(len_str1))

#String maketrans()\ translate() method
print('''\n--- String maketrans()\ translate() Method ---
maketrans() \ translate() - return a translation table that maps each character 
              in their intab string into the character at the same position in the outtab string
            - both intab and outtab must have the same length
            - pass to the translate() function\n''')

intab_str = 'aeiou'
outtab_str = '12345'
str = 'Are you a serious python developer?'
transtab = str.maketrans(intab_str, outtab_str)
print('Original String: ', str)
print('After maketrans() string: ', str.translate(transtab))

intab = 'pqrstuvwxyz'
outtab = '0987654321*'
str = 'The quick brown fox jumps over the lazy dog.'
print('Original String: ', str)
print('After maketrans() string: ', str.translate(str.maketrans(intab, outtab)))

#String replace() method
print('''\n--- String replace() Method ---
replace() - return a copy of the string in which the occurrences of old have been placed with new
          - optionlly restricting the number of replacements to max\n''')

sample_str = 'Are you a serious python programmer?'
print('Original String: ', sample_str)
print('After replacement: ', sample_str.replace('programmer', 'developer'))

#String rfind() method
print('''\n--- String rfind() Method ---
rfind() - return the last index where the substirng str is found or -1 if no such index exists
        - optionally restricting the search to string [beg:end]\n''')

str1 = 'Are you a serious python developer?'
str2 = 'python'
print('Original String: ', str1)
print('find index for "python" in string: ', str1.rfind(str2))
print('find index for "python" in string with index number: ', str1.rfind(str2, 0, 30))
print('find index for "python" in string with index number: ', str1.rfind(str2, 30, 0))

#String rindex() method
print('''\n--- String rindex() Method ---
rindex() - return the last index where the substirng str is found
        - if no such index exists, raise an exception (ValueError: substring not found)
        - optionally restricting the search to string [beg:end]\n''')

str1 = 'Are you a serious python programmer?'
str2 = 'python'
str3 = 'programmer'
print('Original String: ', str1)
print('find index for "python" in string: ', str1.rindex(str2))
print('find index for "programmer" in string: ', str1.rindex(str3))
#print('find index for "python" in string with index number: ', str1.rindex(str2, 0, 10)) #ValueError statement
#print('find index for "programmer" in string with index number: ', str1.rindex(str3, 0, 10)) #ValueError statement

#String split() method
print('''\n--- String split() Method ---
split() - return a list of all the words in the string
        - optionally limiting the number of splits to num\n''')

split_str = 'Are you interested in python programming language?'
print('Original String: ', split_str)
print('After splitting: ', split_str.split())
print('After splitting "programming" with index: ', split_str.split('programming'))
print('After splitting "o" with maxsplit 2: ', split_str.split('o', 2))

#String splitlines() method
print('''\n--- String splitlines() Method ---
splitlines() - returns a list with all the lines in string, 
             - optionally including the line breaks\n''')

splitlines_str1 = r'Python \n multipurpose \nprogramming \nlanguage'
splitlines_str2 = 'Python \n multipurpose \nprogramming \nlanguage'
print('Original String: ', splitlines_str1)
print('After using splitlines(): ', splitlines_str2.splitlines())

#String swapcase() method
print('''\n--- String swapcase() Method ---
swapcase() - returns a copy of the string in which all the case-based characters have had their case swapped\n''')

swapcase_str1 = 'ARE YOU OKAY?'
swapcase_str2 = 'the world is flat, is not?'
swapcase_str3 = 'John Charlie Rocky Snowy'
print('Original String: ', swapcase_str1)
print('After using swapcase(): ', swapcase_str1.swapcase())

print('\nOriginal String: ', swapcase_str2)
print('After using swapcase(): ', swapcase_str2.swapcase())

print('\nOriginal String: ', swapcase_str3)
print('After using swapcase(): ', swapcase_str3.swapcase())

#String zfill() method
print('''\n--- String zfill() Method ---
zfill() - pads string on the left with zeros to fill width\n''')

zfill_str = 'The quick brown fox jumps over the lazy dog.'
print('Original String: ', zfill_str)
print('After using zfill(50): ', zfill_str.zfill(50))
print('After using zfill(70): ', zfill_str.zfill(70))
print('After using zfill(90): ', zfill_str.zfill(90))





