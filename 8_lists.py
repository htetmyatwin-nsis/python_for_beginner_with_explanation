#Python Lists
print('''\n --- Python Lists ---
Python Lists - most versatile datatype
             - comma-separated values (items) between square brackets
             - items in the lists need not be of the same type
             - first index => 0 | second index => 1\n''')

list1 = ['Python', 3.9, 'GoLang', 1.15, 'NodeJS', 15, 'Java', 15]
list2 = [1, 'a', 2, 'e', 3, 'i', 4, 'o', 5, 'u']
list3 = ['Vue', 'React', 'Angular']
print(list1, list2, list3)

#Accessing Values in Lists
print('\n--- Accessing Values in Lists ---')
print('list1[0]: ', list1[0])
print('list2[1] + list2[3] + list2[5] + list2[7] + list2[9]: ', list2[1] + list2[3] + list2[5] + list2[7] + list2[9])

#Updating Lists
print('''\n--- Updating Lists ---
- can update single or multiple elements of lists by giving the slice
- can add to elements in a list with append() method\n''')

print('Original list3: ', list3)
list3[2] = 'Spring'
print('update list3[2]: ', list3)
print('Original list1: ', list1)
list1.append('C#')
print('Add new elements to list1: ', list1)

#Delete List Elements
print('''\n--- Delete List Elements ---
- can use del statement to remove a list element
- can use remove() method \n''')

print('list1: ', list1, '\nlist2: ', list2, '\nlist3: ', list3)
del list1[8]
del list2[0]
del list3[2]
print('After deleting list1[8]: ', list1)
print('After deleting list2[0]: ', list2)
print('After deleting list3[2]: ', list3)

#Basic List Operator
print('''\n--- Basic List Operator ---
+ => concatenation 
* => repetition\n''')

lst1 = [1, 2, 3]
lst2 = ['kotlin', 'swift']
print('Original lst1 and lst2: ', lst1, lst2)
print('After concatenation lst1 and lst2: ', lst1 + lst2)
print('After repetition lst1*3: ', lst1*3)
print('After repetition lst2*2: ', lst2*2)

#Indexing, Slicing and Matrixes
print('''\n--- Indexing, Slicing and Matrixes ---
 - since lists are sequencess, indexing and slicing work the same way for lists\n''')

sample_list = ['Python', 'Kotlin', 'Vue', 'NodeJs', 'Swift', 'React']
print('Original List: ', sample_list)
print('sample_list[3]: ', sample_list[3])
print('sample_list[-2]: ', sample_list[-2], '| #Negative: count from right') #Negative: count from right
print('sample_list[2:]: ', sample_list[2:])

#Built-in List Function & Methods
print('\n--- Built-in List Function & Methods --- \n')

#List len() Method
print('''\n-- List len() Method --
len() - returns the number of elements in the list\n''')

len_lst = ['FrontEnd', 'BackEnd', 'Database', 'Mobile', 'DevOps', 'Cloud']
print('Original String: ', len_lst)
print('lenght of string: ', len(len_lst))

#List max() Method
print('''\n-- List max() Method --
max() - return the elements from the list with maximum value in the list
min() - return the elements from the list with minimum value in the list\n''')

lst1, lst2 = ['kotlin', 'swift'], [1, 2, 3]
print('Original lst1 and lst2: ', lst1, lst2)
print('max value of lst1 and lst2: ', max(lst1), ' | ', max(lst2))
print('min value of lst1 and lst2: ', min(lst1), ' | ', min(lst2))

#List list() Method
print('''\n-- List list() Method --
list() - take sequence type and convert a given tuple or string into list\n''')

sample_tuple = ('aeiou', 'xyz', 'blah blah blah')
sample_str = 'AI / ML'
print('Original tuple and string: ', sample_tuple, ' | ', sample_str)
print('After listing tuple: ', list(sample_tuple))
print('After listing string: ', list(sample_str))

#List append() Method
print('''\n-- List append() Method --
append() - append or update a passed obj into the existing list\n''')

ori_lst = ['Rust', 'WebAssembly', 'C']
print('Original List: ', ori_lst)
ori_lst.append('C++')
print('Updated list with C++: ', ori_lst )

#List count() Method
print('''\n-- List count() Method --
count() - return count of how many time obj occur in list\n''')

count_lst = [1, 'xyz', 2, 'zyx', 3, 1, 'xyz']
print('Original List: ', count_lst)
print('Count for 1 in list: ', count_lst.count(1))
print('Count for xyz in list: ', count_lst.count('xyz'))

#List extend() Method
print('''\n-- List extend() Method --
extend() - append the contents of seq to list\n''')

lst1 = ['Steve', 'Linux', 'Elon']
print('Original List: ', lst1)
lst2 = list(range(3))
lst1.extend(lst2)
print('Extended List with range(3): ', lst1)

#List index() Method
print('''\n-- List index() Method --
index() - return the lowest index in list that obj appears
        - if index not found, return ValueError\n''')

index_lst = ['Lexus', 'Acura', 'Infinity', 'Genesis']
print('Original List: ', index_lst)
print('Index of Acura: ', index_lst.index('Acura'))
#('Index of Maybach: ', index_lst.index('Maybach')) #return ValueError

#List insert() Method
print('''\n-- List insert() Method --
insert() - insert object into list at offset index\n''')

insert_lst = ['Chemistry', 'Physics', 'Biology']
print('Original List: ', insert_lst)
insert_lst.insert(0, 'Mathematics')
print('After inserting Mathematics at index 0: ', insert_lst)
insert_lst.insert(4, 'Economics')
print('After inserting Economics at index 4: ', insert_lst)

#List pop() Method
print('''\n-- List pop() Method --
pop() - remove last obj from the list\n''')

pop_lst = ['Python', 'Kotlin', 'NodeJS', 'Vue', 'React']
print('Original List: ', pop_lst)
pop_lst.pop()
print('After using pop(): ', pop_lst)
pop_lst.pop(2)
print('After using pop(2): ', pop_lst)

#List remove() Method
print('''\n-- List remove() Method --
remove() - object to be removed from the list\n''')

remove_lst = [123, 'xyz', 'abcde', 27]
print('Original List: ', remove_lst)
remove_lst.remove(27)
print('After removing 27: ', remove_lst)
remove_lst.remove('xyz')
print('After removing xyz: ', remove_lst)

#List reverse() Method
print('''\n-- List reverse() Method --
reverse() - reverse objs of list in place\n''')

rev_lst = [1, 2, 3, 4, 5]
print('Original List: ', rev_lst)
rev_lst.reverse()
print('After using reverse(): ', rev_lst)

#List sort() Method
print('''\n-- List sort() Method --
sort() - sorts obj of list\n''')

sort_lst = [2, 11, 5, 3, 7, 17, 19, 13]
print('Original List: ', sort_lst)
sort_lst.sort()
print('After using sort(): ', sort_lst)

sort_lst1 = ['Python', 'Kotlin', 'Swift', 'C#', 'Java', 'NodeJS']
print('Original List: ', sort_lst1)
sort_lst1.sort()
print('After using sort(): ', sort_lst1)