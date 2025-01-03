class Solution:
    # Function to rotate an array by d elements in counter-clockwise direction.
    def rotateArr(self, arr, d):
        n = len(arr)
        d %= n  # Handle cases where d > n

        def reverse(start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        # Step 1: Reverse the first d elements
        reverse(0, d - 1)

        # Step 2: Reverse the remaining n - d elements
        reverse(d, n - 1)

        # Step 3: Reverse the entire array
        reverse(0, n - 1)


# Driver Code Starts
def main():
    try:
        T = int(input("Enter the number of test cases: "))  # Number of test cases
        for _ in range(T):
            print("\nTest case", _ + 1)
            n, d = map(int, input("Enter n (size of array) and d (rotations): ").strip().split())  # Input size of array and d
            A = list(map(int, input("Enter array elements: ").strip().split()))  # Input array

            if len(A) != n:
                raise ValueError("The number of array elements does not match n.")

            print("Original Array:", A)
            print("Rotating by", d, "steps...")

            ob = Solution()
            ob.rotateArr(A, d)

            print("Rotated Array:", " ".join(map(str, A)))  # Print the rotated array

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    main()
