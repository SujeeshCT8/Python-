student = {
    "name":"jhon",
    "age":"20",
    "grade":"A",
}

print(student["name"])
student["citie"] = "newyork"
print(student)
student["grade"]="B" #updating the list by changing the grade

print(student)


#2.Easy-Medium

scores = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 92
}
scores["suj"] = "89"
print(scores)

for key in scores:
    print(key,":",scores[key])