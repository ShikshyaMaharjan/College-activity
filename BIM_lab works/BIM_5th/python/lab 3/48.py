student = {"name": "Ram", "age": 20}
print(student["name"])
print(student["age"])
student["city"] = "Kathmandu"
print(student)
student.pop("age")
print(student)
for key, value in student.items():
    print(key, value)