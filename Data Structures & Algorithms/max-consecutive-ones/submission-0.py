class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currentMax = 0
        bestMax = 0

        for num in nums:
            if num == 1:
                currentMax += 1
            else:
                currentMax = 0
            bestMax = max(bestMax, currentMax)

        return bestMax 

# Inputs: binary array -> 0 1, nums
# Outputs: return the max number of consecutive 1s
# Example
# nums = 1 1 0 1 1 1 
# currentMax = 3
# return currentMax
# currentMax = 2
# bestMax = 0

# Brute force approach:
#   currentMax = 0
#   bestMax = 0
#   for num in nums:
#       if num == 1:
#           currentMax += 1
#       else:
#           currentMax = 0
#       result = max(result, currentMax)
#   return resultMax
# time: O(n)
# space: O(1)