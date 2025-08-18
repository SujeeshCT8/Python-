#ask 3: Keep asking until valid input.

while True:
    try:
        num = int(input("enter a number : "))
        print(f"you entered :{num}")
        break
    except ValueError:
        print("❌ Invalid input, please enter a number!")