class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for x in s:
            if x == '(':
                stack.append(x)
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(x)
        return len(stack)
