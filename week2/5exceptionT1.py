try:
    a = int(input("enter first no : "))
    b = int(input("enter second no : "))
    result = a/b
    print("result :" ,result)
except ValueError:
    print("not a valid number")
    
except ZeroDivisionError:
    print("not divisble by zero")