#3️⃣ Multiple Except Blocks

try:
    a = int(input("enter first no : "))
    b = int(input("enter second no : "))
    result = a/b
    print("Result : ",result)
except ValueError:
    print("please enter valid number only. ")
except ZeroDivisionError:
    print("cannot divide by zero !")
