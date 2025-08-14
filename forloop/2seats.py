#List the even-numbered seats in a cinema row

n = int(input("enter the no of seats u want "))
for i in range(1,n+2):
    if i % 2 == 0:
        print("avialblle seats are ",i)
    else:
        pass