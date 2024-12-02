# Question 1 (Basic):
# Create a dictionary with the following data:
# key: "name", "age", "city"
# value: "Alice", 25, "New York".

# Now, retrieve the value of the key "city".

detail={
    "Name":"Alice",
    "Age": 25,
    "City":"New York"
}
print(detail['City'])




# Question 2:
# How can you add a new key-value pair to the following dictionary?

student = {
    "Name": "Bob",
    "Age": 20,
    "Grade": "A"
}
# Add the key "Subject" with the value "Math" to the dictionary.
student.update({'Subject':'Maths'})
print(student)

# Question 3:
# How would you delete the key-value pair for "Age" from the following dictionary?

student = {
    "Name": "Alice",
    "Age": 25,
    "City": "New York",
    "Subject": "Math"
}
student.remove('Age')
print("student")


# Write a Python program to check if a given key exists in the following dictionary.

student = {
    "Name": "Alice",
    "Age": 20,
    "Grade": "A"
}
# Check for the key "Age" and "School"
print(student.get("Age", "School"))

