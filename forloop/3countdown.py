import time
t = int(input("enter cont down : "))
for i in range(t , 0, -1):
    print(i)
    time.sleep(1)
    if i ==1:
        print(" Liftoff!.🚀")


#The countdown starts at 10 seconds and goes down to 1 second, then says “Liftoff!”.