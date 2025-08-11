n = list(map(int, input("Enter numbers separated by spaces: ").split()))
for i in n:
    count = n.count(i)
    if count == 1:
        print(i, end="are unique")
        break
else:
    print("no unique number presents ")