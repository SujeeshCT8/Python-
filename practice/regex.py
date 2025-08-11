import re
T = int(input("enter the no "))
for i in range(T):
    S = input("enter patterns").strip()
    try:
        re.compile(S)
        print("true")
    except re.error:
        print("false") 