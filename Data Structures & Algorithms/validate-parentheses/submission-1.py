class Solution:
    def isValid(self, s: str) -> bool:
        matchingPairs = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for i in s:
            if i in matchingPairs:
                stack.append(matchingPairs[i])
            else:
                if not stack or stack[-1] != i:
                    return False
                stack.pop()
        return not stack
        

# Inputs: string of s -> s = "( ) { } [ ]"
#           valid only if: brackets are closed by same type 
#                           open brackets are closed in correct order
#                           Close bracket has corresponding open bracket of same type
# Output: return true if s is valid
#           otherwise false

# Example: 
#   s = "([{}])"
#   output = True

# Approach:
#   stack = [ ( [ { ]
#   for string in s:
#       if string == "(":
#           stack.append(string)
#       elif string == "[":
#           stack.append()
#       elif string == "{":
#           stack.append()
#       elif string == "}" and stack[-1] == "{":
#           stack.pop()
#       elif string == ")" and stack[-1] == "(":
#           stack.pop()
#       elif string == "[" and stack[-1] == "]":
#           stack.pop()
#   return not stack
