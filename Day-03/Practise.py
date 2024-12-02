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


student = {
    "Name": "John",
    "Age": 20,
    "Subjects": ["Math", "English", "History"]
}
# Add a new key-value pair: "City" with the value "New York".
# Change the "Age" to 21.
# Add "Science" to the "Subjects" list.

student.update({"City": "New York"})
student.update({"Age": 21})
student["Subjects"].append("Science")  # Add "Science" to the list
print(student)

# Question:

# You have a dictionary with students' names as keys and their scores as values. Write a Python code to:

# Add a new student and their score to the dictionary.
# Modify the score of an existing student.
# Remove a student from the dictionary.
# Display the average score of all students.
# Here’s the sample dictionary:

students_scores = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92
}