'''Question 1:
Write a Python program to add an element at the end of the list using the append() 
method.

Example:

Input: [1, 2, 3] and element 4
Output: [1, 2, 3, 4]'''

num=[3,4,5,2,3,4,5]
num.append(0)
print(num)

'''Write a Python program to remove the first occurrence of a specific element from
the list using the remove() method.

Example:

Input: [1, 2, 3, 4, 3, 5] and element 3
Output: [1, 2, 4, 3, 5]'''

str=[1,2,3,4,5,6,7,8,2,3,2]
str.remove(2)
print(str)

'''Create a tuple with the elements 1, 2, 3, 4, 5. Write a Python program to access
 the 3rd element from the tuple.

Example:

Input: (1, 2, 3, 4, 5)
Output: 3'''
str_input=(3,4,5,6,6,2,1,6,3,9)
num=str_input[2]
print(num)

'''Write a Python program to count the occurrences of a specific element (e.g., 6) 
in a tuple using the count() method.

Example:

Input: (3, 4, 5, 6, 6, 2, 1, 6, 3, 9)
Output: 3 (since 6 appears 3 times)'''
str_input=(9,7,6,8,7,1,2,3,6,6,8)
num=str_input.count(6)
print(num)

'''Let‘s Practice

WAP to ask the user to enter names of their 3 favorite movies & store them in a list.'''
user_movie = input("Enter your favorite movies (separate them with a comma): ").split(',')
print(user_movie)

'''Write a Python program to remove duplicates from a list of movies using the set() method.

Example:

Input: ['Inception', 'Avatar', 'Titanic', 'Avatar', 'The Matrix', 'Titanic']
Output: ['Inception', 'Avatar', 'Titanic', 'The Matrix']'''

str_input= ['Inception', 'Avatar', 'Titanic', 'Avatar', 'The Matrix', 'Titanic']
num= list(set(str_input))
print(num)