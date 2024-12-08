# Simple Python program to find the factorial of a number
num = 4
fact = 1

for i in range (1, num + 1):
    fact *= i
    
print(f"Factorial of the number {num} is {fact}")