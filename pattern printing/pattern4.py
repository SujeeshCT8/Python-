letter = int(input("enter a no "))
for i in range(letter):
    row=[]
    for j in range(1,i+1):
        row.append(str(i))
    print(" ".join(row))

#printing same no in a row 1 in first row 2 in 2 times a row like wise