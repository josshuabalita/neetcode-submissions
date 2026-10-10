class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        sums = 0
        for num in nums:
            sums += num
            self.prefix.append(sums)
    # T O(n)
    # S O(n)

    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefix[right]
        if left > 0:
            leftSum = self.prefix[left - 1]
        else:
            leftSum = 0
        return rightSum - leftSum
        # T O(1)
        # S O(1)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# Inputs: nums: List[int] that handles queries of type:
#               sum of elements of nums between left and right, left <= right
# Goal: Implement the NumArray Class:
#       NumArray(int [] nums): initializes the object using the array of nums
#       int sumRange(int left, int right): returns the sum of elements between left and right
#       [nums[left], nums[left + 1], nums[left + 2], ... ,nums[right]]