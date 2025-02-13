# Time complexity - O(n)
# Space complexity - O(n)

# Approach - Maintain a stack, only append to stack if it is a number. If it is
# an operator, pop top two elements from the stack, perform the operation, and 
# append the result of the operation back to stack. Return top element of the stack.

from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t not in ["+", "-", "*", "/"]:
                st.append(int(t))
            else:
                pop1 = st.pop()
                pop2 = st.pop()
                if t == "+":
                    result = (pop2 + pop1)
                elif t == "-":
                    result = (pop2 - pop1)
                elif t == "*":
                    result = (pop2 * pop1)
                else:
                    result = int(pop2 / pop1) # this was a catch, rest was simple
                st.append(result)
        return st[0]