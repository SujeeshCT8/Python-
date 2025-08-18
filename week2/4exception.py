#5️⃣ Raising Your Own Exceptions

age = int(input("enter your age : "))
if age < 18: 
    raise ValueError(f"age under {age} restircted")