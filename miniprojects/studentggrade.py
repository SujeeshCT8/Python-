student= {}


def add_student():
    name = input("enter student name :")
    grade = input("enter student grade")
    student[name]  = grade
    print("studnet is added !")

def view_student():
    for name, grade in student.items():
        print(f"Name: {name}, Grade: {grade}")


def search_student():
    name =  input("enter a student name :")
    if name  in student:
        print("name :{name} , grade: {grade}")
    else:
        print("student not exists")

while True:
    print("\n--- Student Grade Manager---")
    print("1. Add student")
    print("2. View students")
    print("3. Search student")
    print("4. Exit")    

    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        view_student()
    elif choice =="3":
        search_student()
    elif choice =="4":
        break
        print("Exiting . Goodbye!")
    else:
        print("wrong input !!")

