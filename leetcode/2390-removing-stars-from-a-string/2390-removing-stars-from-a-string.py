class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for x in s:
            if x == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(x)
        return ''.join(stack)

        