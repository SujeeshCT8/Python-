sentence = input("Enter a sentence : ").lower()
Word = sentence.split()
w_count = {}
for w in Word:
    if w in w_count:
        w_count[w] +=1
    else:
        w_count[w] = 1

for word,count in w_count.items():
    if count == 1:
        print(word)