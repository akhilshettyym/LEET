class Solution:
    def pushZerosToEnd(self, arr):
        
        non_zero_pos = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[non_zero_pos] = arr[i]
                non_zero_pos += 1
        while non_zero_pos < len(arr):
            arr[non_zero_pos] = 0
            non_zero_pos += 1
        return arr
    
arr = [3, 5, 0, 0, 4]
sol = Solution()
result = sol.pushZerosToEnd(arr)
print(result)
# Output: [3, 5, 4, 0, 0]