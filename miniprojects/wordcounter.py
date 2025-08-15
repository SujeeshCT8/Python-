#Mini Project: Word Counter time.

sentence = input("Enter a Sentence : ").lower()
word=sentence.split()
print(word)
word_count ={}
for w in word:
    if w in word_count:
        word_count[w] +=1
    else:
        word_count[w] = 1

for w,count in word_count.items():
    print(f"{w}: {count}")