class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if val != nums[i]:
                nums[k] = nums[i]
                k += 1

        return k

# Inputs: nums[]
#         val -> int
# Output: return the number of elements in nums not equal to val
#         k = # of elements != val in nums[]
#         nums = [] -> updated array without the occurences
# Goal: remove all ocurrence of val in nums[] -> removed in place
#       order does not matter
#       we just want the num of elements
# Variables: k = num of elements in nums[] != val
# Example:
#   nums = [3 2 2 3]
#   nums[k] = [2 2 0 0]
#   val = 3
#   return k = 1, nums = [2 2 _ _]

# Brute Force Approach - Already Optimal:
#   k = 0
#   for i in range(len(nums)):
#       if val != nums(i):
#           nums[k] = nums[i]
#           k += 1
#   return k
# Time: O(n)
# Space: O(1)