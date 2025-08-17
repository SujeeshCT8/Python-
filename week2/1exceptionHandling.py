#What is an Exception?
#An exception is an error that happens while a program is running.
try:
    num = int(input("enter a number : "))
    print("you entered :",num)
except ValueError:
    print("thats not a number !")