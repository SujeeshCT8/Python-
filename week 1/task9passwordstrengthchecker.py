password = input("Enter your password: ")

special_characters = "!@#$%^&*()-_=+[]{};:,.<>?/"

score = 0

if len(password) >= 8:
    score += 1
if any(char.isupper() for char in password):
    score += 1
if any(char.islower() for char in password):
    score += 1
if any(char.isdigit() for char in password):
    score += 1
if any(char in special_characters for char in password):
    score += 1

if score == 5:
    print("Strong password ✅")
elif score >= 3:
    print("Medium password ⚠️")
else:
    print("Weak password ❌")
