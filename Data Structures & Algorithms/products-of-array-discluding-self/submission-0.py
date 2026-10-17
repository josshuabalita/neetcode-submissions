class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res

# T O(n)
# S O(n) for result array

# Inputs: List[int] -> nums
# Outputs: return an array of output: List[int] -> output
#           output[i] = product of all elements of nums except nums[i]
#           each product is guarantedd to fit in a 32 bit int

