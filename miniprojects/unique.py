# 🚀 Mini Challenge
# Write a Python program that:
# Asks the user to enter 5 numbers (store them in a list)
# Convert the list to a set to remove duplicates
# Print the unique numbers
# 💡 Hint: Use input() in a loop and set() conversion.

numbers =[]
for i in range(5):
    user_input = int(input(f"enter  number {i+1}  of 5: "))
    numbers.append(user_input)
print(numbers)
    
unique_numbers = set(numbers)

print("original lists:" ,numbers)
print("After removing duplicates ",sorted(unique_numbers))