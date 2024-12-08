# Adding two numbers using functions
def add(num1,num2):
    return (num1+num2)

num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))

sum = add(num1, num2)

print(f"Sum of {num1} + {num2} is {sum}")