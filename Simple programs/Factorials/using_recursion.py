# Get Factorial of a Number using a Recursive Approach
def factorial(num):
    return 1 if (num==0 or num==1) else num * factorial (num-1)
num = 4
print(f"Factorial of the number {num} is {factorial(num)}")