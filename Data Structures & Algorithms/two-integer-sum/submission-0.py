class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in numsMap:
                return [numsMap[diff], i]
            numsMap[n] = i
# T: O(n)
# S: O(n)

# Inputs: array of int nums -> nums[int]
#           target: int
# Output: return the indeces of i and j, i + j = target and i is not equal to j
#           we can assume that each input has one pair
#           return the answer with smallest index first -> [0, 1]