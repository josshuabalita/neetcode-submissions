class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans

# Inputs: array[nums] of length n -> nums[n.length]
# Output: create ans[2n] -> where ans[i] == nums[i]
#           ans[i + n] == nums[i] for 0 <= i < n, 0 indexed
#           ans -> concat of 2 nums arrays
#           return ans

# Example:
#   nums = [1 4 1 2]
#   output = [1 4 1 4 1 4 1 2]
#   1 4 1 2 1 4 1 2

# Solution:
#   ans = []                      # new list
#   for num in nums: ans.append(num)   # first copy   -> O(n)
#   for num in nums: ans.append(num)   # second copy  -> O(n)
#   return ans
# Time:  O(n)  (each element handled once)
# Space: O(n)  (output of length 2n)