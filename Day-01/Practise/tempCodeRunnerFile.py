str_input=input("Enter Your Number Here:")

rev=str_input[::-1]

if str_input==rev:
    print("It is Palindrome"),
else:
    print("It is not a palindrome")