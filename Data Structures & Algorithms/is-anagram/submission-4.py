class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sMap, tMap = {}, {}
        for ch in s:
            if ch not in sMap:
                sMap[ch] = 1
            else:
                sMap[ch] += 1
        
        for ch in t:
            if ch not in tMap:
                tMap[ch] = 1
            else:
                tMap[ch] += 1
        
        return sMap == tMap

# T O(n + m)
# S O(n + m) -> O(1), we have 26 letters in alphabet
#                       no radical increase in size

# Input: strings -> s 
#                   t
# Output: return True if s and t are anagrams of each other
#           otherwise return false
# Terms: Anagram -> if they contain the same char, each char appears the same, regardless
