student = {}

while True:
    name = input("Enter student name (or type 'done' to finish): ")
    if name == "done" :
        break

    grade =int(input("enter the grade of student"))
    student[name]=grade

    
while True:
    if 90 <= grade <= 100:
        letter ="A"
    elif 80 <= grade <= 89:
        letter ="B"
        
    elif 70 <= grade <= 79:
        letter ="C"
       
    elif 60 <= grade <= 69:
        letter ="D"
        
    else:
        letter ="E"
        
    break
    
print("------student gradebook------")
for name,grade in student.items():
    print(f"Student: {name} | mark: {grade} | grade: {letter}")
