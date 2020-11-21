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
print('str1[0:4] and str2[5:6]: ', str1[0: 4], str2[5: 6])
print('Raw String: ', r'C:\\blah blah')
print('Item name is %s and price is %d$ ! ' %('Zara Chino', 79))

