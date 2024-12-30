n = int(input("Enter the number of elements: "))
print("Enter elements:")
lst = []

for i in range(n):
    lst.append(int(input()))

# Initialize largest and second largest
largest = second_largest = None

for num in lst:
    if largest is None or num > largest:
        second_largest = largest
        largest = num
    elif num != largest and (second_largest is None or num > second_largest):
        second_largest = num

# Print the result
if second_largest is not None:
    print("Second largest element is:", second_largest)
else:
    print("No second largest element exists.")