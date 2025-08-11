#Create a list of your 5 favorite movies, then:
#Add 2 more
#Remove 1
#Print them in reverse order
#Make a tuple of 3 cities you want to visit, loop through and print them.
#Create a set of numbers, try adding a duplicate, and see what happens.
#🚀 Mini Challenge

moveis =[]
for i in range(5):
    user_input = input(f"enter your favourite movies  {i+1} ")
    moveis.append(user_input)
print("your favriote movies are :" ,moveis)
if "ram" in moveis:
    moveis.remove("ram")
    print("i like remvoved ", moveis)
moveis.reverse() #reversing of the list
print("reversed ",moveis)

for vedio in moveis:# to vist a each item in the list and print it
    print(vedio) 


#2.Make a tuple of 3 cities you want to visit, loop through and print them.

cities =["london","paris","spain"]
for city in cities:
    print(city)

#3.Create a set of numbers, try adding a duplicate, and see what happens.

numbers = {1, 2, 3}
print("Original set:", numbers)
numbers.add(5) 
print("After adding duplicate 2:", numbers)
numbers.add(4)
print("After adding 4:", numbers)
