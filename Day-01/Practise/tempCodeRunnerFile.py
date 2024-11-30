
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
