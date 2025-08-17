fword = input("enter the word to find the frequent one ").lower()
word = fword.split()
word_count = {}
for w in word:
    if w in word_count:
        word_count[w]+=1
    else:
        word_count[w]=1

most_frequent = max(word_count,key=word_count.get)
print(f"Most frequent word: {most_frequent} : {word_count[most_frequent]}")

if word_count[most_frequent]>3:
    print(f"{most_frequent}'appear more than 3 times")
else:
    print(f"{most_frequent}'lees than 3 times")
