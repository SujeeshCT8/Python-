letter = int(input("Enter no: "))

for i in range(letter+1):
    spaces = " " * (letter - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)


#for reversing the row just make the range(letter,0,,-1)