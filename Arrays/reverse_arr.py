class Solution:
    def reverseArray(self, arr):
        start = 0
        end = len(arr)-1
        while start < end :
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        return arr
if __name__ == "__main__":
    # Example 1: Reversing an array
    arr = [1, 2, 3, 4, 5]
    sol = Solution()  # Create an object of the Solution class
    reversed_arr = sol.reverseArray(arr)  # Call the reverseArray method
    print("Reversed array:", reversed_arr)  # Output the reversed array
    
    # Example 2: Reversing an array with even number of elements
    arr2 = [10, 20, 30, 40]
    reversed_arr2 = sol.reverseArray(arr2)
    print("Reversed array:", reversed_arr2)  # Output the reversed array

    # Example 3: Edge case: empty array
    arr3 = []
    reversed_arr3 = sol.reverseArray(arr3)
    print("Reversed array:", reversed_arr3)  # Output the reversed array

    # Example 4: Edge case: single-element array
    arr4 = [99]
    reversed_arr4 = sol.reverseArray(arr4)
    print("Reversed array:", reversed_arr4)  # Output the reversed array