class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # T O(n), S O(n)
        stack = []
        for tok in tokens:
            if tok == "+":
                valOne = stack.pop()
                valTwo = stack.pop()
                stack.append(valTwo + valOne)
            elif tok == "*":
                valOne = stack.pop()
                valTwo = stack.pop()
                stack.append(valTwo * valOne)
            elif tok == "-":
                valOne = stack.pop()
                valTwo = stack.pop()
                stack.append(valTwo - valOne)
            elif tok == "/":
                valOne = stack.pop()
                valTwo = stack.pop()
                stack.append(int(valTwo / valOne))
            else:
                stack.append(int(tok))
        return stack.pop()

# Inputs: tokens -> takes valid arithmetics 
# Goal: Expression in reverse polish notation
# Output: return the integer representing the evaluation
