def is_prime(n):
    if n <= 1:
        return "Not Prime"
    
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    
    return "Prime"

# Get input from the user
num = int(input("Enter a number: "))

# Call the function and print result
result = is_prime(num)
print(result)
