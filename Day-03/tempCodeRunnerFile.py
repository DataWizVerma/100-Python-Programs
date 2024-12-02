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
