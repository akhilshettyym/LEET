# Add Two Numbers Using Recursive Function
def add_numbers_recursive(x, y):
    if y == 0:
        return x
    else:
        return add_numbers_recursive(x+1, y-1)

num1 = 30
num2 = 30

sum = add_numbers_recursive(num1, num2)
print(f"Sum of {num1} + {num2} is {sum}")