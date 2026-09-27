class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1

        for i in range(len(arr) - 1, -1, -1):
            newMax = max(rightMax, arr[i]) 
            arr[i] = rightMax 
            rightMax = newMax 
        return arr

# Inputs: arr[]
# Output: return arr[]
# Goal: replace each element in arr[] with the greatest element on its right
#       replace the last element with -1
# Example:
# arr = [2 4 5 3 1 2] 
# Output = [5 5 3 2 2 -1]
# Variables: currentGreatest = 0
