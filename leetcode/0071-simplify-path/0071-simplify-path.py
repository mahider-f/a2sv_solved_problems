class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        for x in path:
            if x =="..":
                if stack:
                    stack.pop()
            elif x !="." and x != "":
                stack.append(x)
        return '/'+'/'.join(stack)
