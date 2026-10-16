class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res +=(str(len(s)) + "#" + s)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res

# T O(n)
# S O(n)

# Input: encode a list of strings to string
#       the new encoded string is decoded back -> back to the list of original strings
#       encode:
#           returns the encoded string
#       decode(receiver):
#           returns the decoded strings
#       
#       decoded_strs == same input as strs in Machine 1 (encode)

