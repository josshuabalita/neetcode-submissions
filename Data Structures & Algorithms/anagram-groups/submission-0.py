class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            group[tuple(count)].append(s)
        return list(group.values())

# T (m * n)
# S (n)

# Input: array of strings -> List[strs]
# Goal: group all anagrams together into a sublists
# Output: return the output, order does not matter
# Terms:
#   Anagram: string containing exact same chars with another string
#               order of strings does not matter
#   Sublist: List[[strings: [str1, str2]]]

# Example 1
# strs = ["act","pots","tops","cat","stop","hat"]


# Brute force using sort -> m * nlogn
# strs = ["act", "cat", "hat", "pots", "stop", "tops"]
# [act, cat], [hat], [pots, stop, tops]