student={
    "Name":"Kumar Verma",
    "marks":{
        "chemistry": 23,
        "physics":20,
        "Maths":33
    }
}
new_dict={"Name":'kumar verma',
          'age':23,
          "city":'Lucknow'}
student.update(new_dict)

print(student)
print(student.get('Name'))