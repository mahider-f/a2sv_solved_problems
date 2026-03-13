class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        ans = ""
        for x in s:
            if x.isdigit():
                num = num*10 + int(x)  
            
            elif x == '[':
                stack.append((ans,num))
                ans = ''
                num = 0
            elif x == ']':
                cur = stack.pop()
                ans = cur[0] + ans * cur[1]
            else: 
                ans+=x

        return ans


