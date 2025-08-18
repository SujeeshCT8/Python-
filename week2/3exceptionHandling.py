#4️⃣ Using Else and Finally
#else: Runs if no exception occurs
#finally: Runs no matter what (good for cleanup)

try:
    a = int(input("Enter a Number : "))
except ValueError:
    print("not a valid no ")
else:
    print("you entered ",a)
finally:
    print("program finised ")