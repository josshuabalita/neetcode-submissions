class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = set()

        for num in nums: 
            if num in duplicates:
                return True
            duplicates.add(num)
        return False

# inputs: nums[int]
# output: if value appears more than once return true
#           otherwise return false, if value <= 1
# Example:
# nums = [1 2 3 3]
#       1 = 1 -> duplicates[1]
#       2 = 1 -> duplicates[1,2]
#       3 = 1 -> duplicates[1,2,3]
#       3 = 2 -> 
# return true
# Brute force approach:
#   duplicates = []
#   for num in nums:
#       if num not in duplicates:
#           duplicates.append(num)
#       else if num in duplicates: 
#           return true
#   return false
# Time Complexity: O(n2)

# Improve our solution: hash set\
# HashSet Approach:
#   duplicates = set() 
#   for num in nums: -> O(n)
#       if num in duplicates: -> O(1)
#           return True
#       duplicates.add(num)
#   return False
# Time Complexity: O(n)
# Space Complexity: O(n)
