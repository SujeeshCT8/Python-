#1.Safe Calculator — A calculator that does +, -, *, / safely using exception handling.


while True:
    try:
        num1 = int(input("enter the first no: "))
        num2 = int(input("enter the second no: "))
        op = input("which operation they want (+, -, *, /).")
        
        if op == '+':
            print("Addition - result = ",num1+num2)
        elif op == '-':
            print("Substract- result =",num1-num2)
        elif op == '*':
            print("Multiplication - result :",num1*num2)
        elif op == '/':
            print("Divison - result :",num1/num2)
        else:
            print("(print invalid operation")
        
        ask = input("wants to calculate again.?").lower()
        if ask != 'yes':
            break

        print("Ended")
            
    except ValueError:
        print("enter nos only ! ")
    except ZeroDivisionError:
        print("Cant divided by 0")

    