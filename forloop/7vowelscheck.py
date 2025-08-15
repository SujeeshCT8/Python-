#Vowel Counter


text = input("enter a string : ").lower()
vowels = "aeiou"
count=0

for ch in text:
    if ch in vowels:
        count +=1
print("total no of vowels present : ",count)

#another vesion 


#text = input("Enter a string: ")
#vowels = "aeiou"
count = sum(text.count(v) for v in vowels)
print("Number of vowels present are:", count)
