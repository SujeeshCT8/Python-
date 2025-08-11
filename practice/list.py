#list practice
single =("only_one",)
print(type(single))

numbers = {1, 2, 3, 4, 4, 5}
print(numbers)

numbers.add(7)
print(numbers)

for num in numbers.copy():
    if num == 3:
        numbers.remove(3)
        print(numbers)
