#Take a string from the user and print:
#1.The first character
#2.The last character
#3.The string in reverse

text = input("enter your string ")
print(text[0])
print(text[-1])
print(text[::-1])


#Task 2: Count how many times "a" appears in "banana"
word = input("eneter a string to count Letters : ")
letter = input("enter which letter u want to check : ")
if letter == 'a':
    print(word.count('a'))
elif letter == 'b':
    print(word.count('b'))
else:
    print("loading....")

print(word.upper())
print(word.lower())
