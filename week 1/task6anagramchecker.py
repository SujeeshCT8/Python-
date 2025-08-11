n = input("enter the first word :").split()
s = input("enter the second word :").split()
if sorted(n) == sorted(s):
    print(n,s,"anagram")
else:
    print("not anagram")