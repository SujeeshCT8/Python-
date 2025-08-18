a = int(input("enter a positve no : "))
if a < 0:
    raise ValueError("the no is negative")
else:
    print(f"you have enterd : {a}")
    