print('''\n--- Loops ---\n
- to execute a statement or group of statements multiple times
* (while) loop 
=> repeat a statement while a given condition is TRUE
=> test the condition before executing the loop body\n

* (for) loop
=> execute a sequence of statements multiple times

* nested loops
=> one or more loop inside any another (while) or (for) loop\n''')

#while loop statements
print('---while loop---\n')
count = 0
while(count < 10):
    print('The count is: ', count)
    count = count + 1
print("Good bye!")

#for loop statements
print('\n---for loop---\n')

for var in list(range(10)): #range() generates integers starting with 0 upto n-1
    print(var)

for letter in 'Are you a python programmer?':
    print('Current letter: ', letter)

cars = ['Lexus', 'Acura', 'Infinity', 'Mercedes-Benz', 'BMW', 'Audi']
for car in cars:
    print('Current car: ', car)

#another way
print('\n--- Another Way --- \n')
sport_cars = ['Acura NSX', 'Nissan R35', 'BMW M4']
for sc in range(len(sport_cars)):
    print('Current sport car: ', sport_cars[sc])

#using decision statement with loops
print('\n--- Using Decision statement with loops ---')
numbers = [1, 2, 4, 6, 8, 12, 14, 15, 16, 20]
for num in numbers:
    if num%4 == 0:
        print('Current number: ', num)

#nested loops
print('\n--- Nested Loops--- \n')
print('First Example')
for i in range(1, 5):
    for j in range(1, 3):
        k = i*j
        print(k)

print('\nSecond Example')
for x in range(1, 3):
    for y in range(5, 7):
        z = x * y
        print(z)

#Loop Control Statements
print('''\n--- Loop Control Staements---\n
* (break) 
=> terminate the loop and transfer execution to the following loop immediately
* (continue) 
=> cause the loop to skip the remainder of its body & retest immediately its condition
* (pass)
=> used when a statement is required syntactically but you do not want any command or code to execute''')

print('\n---Break control => premature termination of the current loop---\n')
for letter in 'Python':  #first example
    if letter == 'h':
        break

    print('Current letter: ', letter)

var = 10 #second example
while var > 0:

    var = var - 1
    if var == 5:
        break

    print('current variable value: ', var)

print('End')

print('\n---continue control => return the control to the beginning of the current loop---\n')
for letter in 'Python':  # first example
    if letter == 'h':
        continue

    print('Current letter: ', letter)

var = 10  # second example
while var > 0:

    var = var - 1
    if var == 5:
        continue
    print('current variable value: ', var)

print('End')

print('\n---Pass control => null operation, nothing happens when it executes---\n')
for letter in 'Python':
    if letter == 'h':
        pass
        print('This is pass block')

    print('Current letter: ', letter)


#Infinite loop
print('\n--- infinite loop---\n')
var = 1
while var == 1:
    num = int(input("Enter a number: "))
    print('You entered: ', num)
    print('Good Bye!')