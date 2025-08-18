while True:
    try:
        a = int(input("enter a no : "))
        if a < 0:
            print("warning not a postive no")
        else:
            print(f"you enterd {a}")
            break
    except ValueError:
        print(f"entered no is not a number ")
