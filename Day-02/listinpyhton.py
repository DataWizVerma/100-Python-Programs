# Write a Python program that takes a list of numbers and returns the sum of all the elements in the list.

# Example:

# Input: [1, 2, 3, 4, 5]
# Output: 15

num=[2,3,1,4,5,5]
strr=sum(num)
print(strr)

'''Question 2:
Write a Python program that takes a list of numbers and returns a new list containing only
the even numbers from the original list.

Example:

Input: [1, 2, 3, 4, 5, 6]
Output: [2, 4, 6]'''

str_input = [3, 4, 4, 3, 2, 6, 8, 7, 9]
even_numbers = [num for num in str_input if num % 2 == 0]
print(even_numbers)

'''Question 1:
Given a list, write a Python program to slice the list and return a sublist from 
the 2nd element to the 5th element (inclusive).

Example:

Input: [10, 20, 30, 40, 50, 60, 70]
Output: [20, 30, 40, 50]'''

str_input=[30,20,50,40,20,80,90]
num=str_input[1:6]
print(num)

'''
Question 2:
Write a Python program to slice the list and return a sublist that contains the
last three elements of the list.

Example:

Input: [10, 20, 30, 40, 50, 60, 70]
Output: [50, 60, 70]'''
str_input = [30, 20, 50, 40, 20, 80, 90]
num = str_input[-3:]  
print(num)
