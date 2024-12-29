# Program to find prime numbers in a range
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for num in range(start, end + 1):
    if num > 1:  # Prime numbers are greater than 1
        for i in range(2, int(num ** 0.5) + 1):  # Check divisors up to sqrt(num)
            if num % i == 0:
                break
        else:
            print(num, "is a prime number")