import math
import os
import time
import sys
#printing star in a simple way
numbers = int(input("enter a number to print stars "))
for i in range(numbers):
    print("*"*i)
#pyramid printing
star = int(input("eneter how many stars  to print "))
row = int(input("enter the number of rows to print"))
for i in range (star,row+1):
    print(" " *(row -i) + "*" *(2*i-1))


# donut 

A, B = 0, 0

while True:
    # No os.system('clear') here!
    z = [0] * 1760
    b = [' '] * 1760
    for j in range(0, 628, 7):
        for i in range(0, 628, 2):
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(40 + 30 * D * (l * h * m - t * n))
            y = int(12 + 15 * D * (l * h * n + t * m))
            o = int(x + 80 * y)
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            if 1760 > o > 0 and D > z[o]:
                z[o] = D
                b[o] = ".,-~:;=!*#$@"[N if N > 0 else 0]
    
    sys.stdout.write("\x1b[H")  # Move cursor to top-left without clearing screen
    for k in range(1760):
        sys.stdout.write(b[k] if k % 80 else '\n')
    sys.stdout.flush()

    A += 0.04
    B += 0.02
    time.sleep(0.05)  # Adjust speed


    