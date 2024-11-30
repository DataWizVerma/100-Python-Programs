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
