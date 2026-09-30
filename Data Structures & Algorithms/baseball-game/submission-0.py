class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(stack[-1] * 2) 
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)
# Time: O(n)
# Space: O(n)


# Inputs: List[strings] -> operations: List[str]
#                           operations[i] -> ith operation apply to the record
#                                         -> integer x, record as a new score of x
#                                         -> + sum of prev two scores
#                                         -> D double of prev score
#                                         -> C remove from the prev score
# Output: sum of all scores after applying the operations
# More info: scorekeeping, beginning of game we start with an empty record
# Example:
#   operations = [1 2 + C 5 D] => 1 2 (+ == 3) (C != 3 -> 1 2) 5 (D == 10) == 18  
#   Output = 18

# Approach:
#   stack = []
#   for ops in operations:
#       if ops == "+":
#           stack.append(stack[-1] + stack[-2])
#       elif ops == "D":
#           stack.append(stack[-1] * 2) 
#       elif ops == "C":
#           stack.pop()
#       else:
#           stack.append(int(ops))
#   return sum(stack)