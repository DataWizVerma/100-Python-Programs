# 1. Find the length of the longest word in a sentence.
# Question:
# Write a Python function that takes a sentence as input and returns the length of the longest word in that sentence.

name=input("Enter Your name here:")
le=len(name)
print("Your name is:",name)
print("And length is:",le)


# Input the sentence
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Find the longest word
longest_word = max(words, key=len)

# Get the length of the longest word
length_of_longest = len(longest_word)

# Print the result
print("The longest word is:", longest_word)
print("The length of the longest word is:", length_of_longest)


# Question:
# Write a Python function that takes a string as input and returns a new string with the first 
# 5 characters of the input string. If the string has fewer than 5 characters, return the entire string.
name = input("Enter your name here: ")
print(name[:5])

'''Write a Python function that takes a string and returns a new string where all occurrences
 of the letter 'a' are replaced with 
'z', but only if 'a' is in lowercase. The function should leave uppercase 'A' unchanged.'''
str=input("Enter Your Name here: ")
num=str.replace('a','z')
print(num)

'''Write a Python function that takes a string and returns the number of vowels (a, e, i, o, u)
 in the string, regardless of case (both uppercase and lowercase vowels should be counted).'''
str_input=input("Enter Your Name Here: ")
vowels=str_input.count('a','A', 'e','E', 'i',"I", 'o',"O", 'u',"U")
print(str_input)
print(vowels)