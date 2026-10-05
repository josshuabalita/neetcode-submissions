class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsMap = {}
        for num in nums: 
            if num not in numsMap:
                numsMap[num] = 1
            else:
                numsMap[num] += 1
                return True
        return False
# T: O(n)
# S: O(n)
        
# Inputs: array of nums -> nums: []
# Output: return true -> if value contains a duplicate -> key(int) : val(int) > 1
#         otherwise false
