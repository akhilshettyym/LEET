class Solution:
    def getSecondLargest(self, arr):
        largest = second_largest = float('-inf')
        
        for num in arr:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num != largest:
                second_largest = num
            
        return second_largest if second_largest != float('-inf') else -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.getSecondLargest([12, 35, 1, 10, 34, 1]))