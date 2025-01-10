def Selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = list(map(int, input("Enter the elements of the array seperated by space :").strip().split()))
print("Original array :", arr)
sorted_arr = Selection_sort(arr)
print("Sorted array :", sorted_arr)