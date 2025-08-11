word = input("enter words seprated by spaces: ").split()
for i in word:
    count = word.count(i)
    print(i,count)