# Python Program to Check Prime Number

num = int(input("Enter a number: "))

# A number less than 2 is not prime
if num < 2:
    print(f"{num} is not a prime number")
else:
    # Check if the number is divisible by any number from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
