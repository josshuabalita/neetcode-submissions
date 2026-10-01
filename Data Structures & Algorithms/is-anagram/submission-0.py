class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# Inputs: s 
#         t
# Outputs: if both strings are annagrams of each other -> return true
#           otherwise -> return false
# What is an annagramm?
#   both strings contains the same chars, len of s string = len of t string 
#   regardless of order
# Example
#   s = racecar     t = carrace
#       e = 1           e = 1
#       c = 2           c = 2
#       a = 2           a = 2 
#       r = 2           r = 2
#  return true
# aaccerr
# aaccerr

# Brute force approach:
#   sorted s = sorted(s) -> O(n log n)
#   sorted t = sorted(t) -> O(n log m)
# Complexity = O(nlogn + nlogm)
# Space = O(1)

# HashMap:
#   map_s, map_t = {}, {}
#   if len(s) != len(t)
#       return False
#   for i in range(len(s)):
#       map_s[s[i]] = 1 + map_s.get[]
