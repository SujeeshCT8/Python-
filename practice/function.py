a=int(input("enter a no "))
b=int(input("enter a no "))

def greet():
    sum = a+b
    print("result =" ,sum)

greet()

#Square funtion
def square(n):
    return n*n
for i in range(1,6):
    print(square(i))

#TASK TO MULTIPY    

def mul(a,b):
    return a*b

result = mul(2,5)
print(result)


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
