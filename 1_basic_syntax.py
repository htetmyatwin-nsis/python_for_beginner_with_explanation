#Python identifiers
print('\n---Python Identifiers---\n')
print("""- a name used to identify a variable, function, class, module or other object
- start with a letter A to Z or a to z or an underscore(_) followed by zero or more letters, underscores and digits (0 to 9)
- not allow punctuation characters such as @, $, and % within identifiers
- case sensitive programming language \n\n
""")

#Naming Conventions for Python identifiers
print('---Naming Conventions---\n')
print("""- Class names start with an uppercase letter
- All other identifiers start with a lowercase letter
- Starting an identifiers with a single leading underscore indicates that the identifiers is private
- Starting an identifiers with two leading underscores indicates a strong private identifier
- If the identifier also ends with two trailing underscores, the identifiers is a language-defined special name\n\n""")

#Reserved Words
print('---Reserved Words---\n')
reserved_word = ['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'Not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']
for rw in reserved_word:
    print(rw + '\n')

#Quotation in Python
print('---Quotation in Python---\n')
print("""- single (') , doubel(") and triple(''') quotes to denote string literals, as long as the same type of quote starts and ends the string.
- triple quotes are used to span the string across multiple lines\n""")

word = "'word'"
sentence = ' "This is a sentence" '
paragraph = ''' """This is a paragraph. It is 
made up of multiple lines and sentences. """ '''

print(word + '\n')
print(sentence + '\n')
print(paragraph + '\n\n')

#Comments in Python
print('---Comments in Python---\n')
print('- a hash (#) sign is used to comment and python interpreter ignores it\n')

print('''print("Hello, Python!") #First Comment \n
print("Python for multi-purposes") #Second Comment \n
print("Strong for Artificial Intelligence(AI), Machine Learning(ML), Deep Learning(DL) and Data-Science(DS)") #Third Comment \n''')

