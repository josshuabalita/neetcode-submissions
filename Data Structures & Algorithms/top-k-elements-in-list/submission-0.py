class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            numsMap[num] = numsMap.get(num, 0) + 1
        for num, count in numsMap.items():
            freq[count].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
# Inputs: nums: List[nums]
#           int: k
# Output: return k 
#           where k is the most frequent element in nums array
#           we may return output in any order
#           answer is always unique!
