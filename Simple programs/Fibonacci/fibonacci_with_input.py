def fibonacci(n):
    if n <= 0:
        print("Invalid input !")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n = int(input("Enter a number to find fibonacci :"))
print(fibonacci(n))