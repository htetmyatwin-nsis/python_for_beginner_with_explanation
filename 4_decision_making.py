print('''\n---Decision Making---\n
Python Programming Language assumes: 
- any non-zero and non-null values ar TRUE
- any zero or null values as FALSE value\n
* if statements
* if...else statements
* nested if statements''')

#if statements
print('\n--- if ---\n')
amount = 10
if amount:
    print('amount is', amount)

discount = 0
if discount:
    print('Disount is', discount)  #not execute => value : FALSE
print('Discount: zero')

#if...else statements
print('\n--- if...else ---\n')
amount = int(input("Enter amount: "))
if amount < 1000:
    discount = amount * 0.05
    print("Discount: ", discount)
else:
    discount = amount * 0.1
    print('Discount: ', discount)

print('Your Amount: ', amount, "\nNet Cost: ", amount - discount)

#elif statements
print('\n--- if...elif...else ---\n')
amount = int(input('Enter amount: '))
if amount < 1000:
    discount = amount * 0.05
    print('Discount: ', discount)
elif amount < 5000:
    discount = amount * 0.1
    print('Discount: ', discount)
else:
    discount = amount * 0.15
    print('Discount: ', discount)

print('Your Amount: ' , amount, '\nNet Cost: ', amount-discount)

#nested if statements
print('\n--- nested if ---\n')
num = int(input("Enter number: "))
if num%2 == 0:
    if num%3 == 0:
        print(num, 'is divisible by 2 and 3.')
    else:
        print(num, 'is divisible by 2, not divisible by 3.')
else:
    if num%3 == 0:
        print(num, 'is divisible by 3, not by 2.')
    else:
        print(num, 'is not divisible by 2 and 3.')

