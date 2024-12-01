'''Question:
Write a Python program that takes a number as input and checks if the 
number is positive, negative, or zero. Print a corresponding message based 
on the condition.'''

num=float(input("Enter Your Number here:"))
if num>0:
    print(num,"Your Number is Positive"),
elif num<0:
    print(num,"Your Number is Negative"),
else:
    print(num,"Your Number is Zero")

'''Write a Python program that takes a number as input and checks 
whether the number is even or odd.
 Print "Even" if the number is even and "Odd" if the number is odd.'''    
num=int(input("Enter Your Number Here: "))
if (num%2==0):
    print("Your Number is Even")
else:
    print("Your Number is Odd")


'''Write a Python program that takes a number as input and checks whether it 
is a multiple of both 3 and 5, only 3, only 5, or neither. Print the corresponding
message for each case:

If it's a multiple of both 3 and 5: "Multiple of both 3 and 5"
If it's only a multiple of 3: "Multiple of 3"
If it's only a multiple of 5: "Multiple of 5"
If it's neither: "Not a multiple of 3 or 5"'''

num=int(input("Enter Your Number here:"))

if(num%3==0 and num%5==0):
    print("Multiple of both 3 and 5"),
elif(num%3==0):
    print("Multiple of 3"),
elif(num%5)==0:
    print("Multiple of 5"),
else:
    print("Not a multiple of 3 or 5")

'''Write a Python program that takes a string as input and checks if it is a palindrome.
 A palindrome is a word, phrase, or sequence that reads the same backward as forward 
 (ignoring spaces, punctuation, and capitalization).

For example:

"madam" is a palindrome.
"hello" is not a palindrome.
Print "Palindrome" if the string is a palindrome, otherwise print "Not a palindrome".'''

str_input=input("Enter Your Number Here:")

rev=str_input[::-1]

if str_input==rev:
    print("It is Palindrome"),
else:
    print("It is not a palindrome")

'''Question:
Write a Python program that takes a string as input and counts the frequency
 of each character 
in the string (ignoring spaces). Print the frequency of each character.'''
# Take input from the user
input_string = input("Enter a string: ")

# Remove spaces from the input string
input_string = input_string.replace(" ", "")

# Create a dictionary to store the frequency of each character
frequency = {}

# Iterate through each character in the string
for char in input_string:
    if char in frequency:
        frequency[char] += 1  # If the character is already in the dictionary, increase the count
    else:
        frequency[char] = 1  # If the character is not in the dictionary, add it with a count of 1

# Print the frequency of each character
for char, count in frequency.items():
    print(f"{char}: {count}")
