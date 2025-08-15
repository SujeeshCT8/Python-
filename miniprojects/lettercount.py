character = input("enter a word to count : ").lower()
w_count = {}
for i in character:
    if i in w_count:
        w_count[i] +=1
    else:
        w_count[i] =1
print(w_count)

for i,w in w_count.items():
    print(f"{i} : {w}")