letter = int(input("Enter a number: "))
for i in range(1, letter + 1):  # outer loop for rows
    row = []
    for j in range( 1,i + 1):   # inner loop for numbers in each row
        row.append(str("*"))
    print(" ".join(row))
