def bubble_sort(arr):
    n = len(arr)
    for i in range (n):
        for j in range (0, n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

arr = list(map(int, input("Enter the elements of the array seperated by space :").strip().split()))
print("Original array :", arr)
sorted_arr = bubble_sort(arr)
print("Sorted array :", sorted_arr)