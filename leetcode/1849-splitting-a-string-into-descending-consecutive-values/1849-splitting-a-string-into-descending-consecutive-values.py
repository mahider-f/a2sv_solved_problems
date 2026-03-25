class Solution:
    def splitString(self, s: str) -> bool:
        
        def dfs(rest, need):
            if rest == "":
                return True
            
            for i in range(1, len(rest) + 1):
                num = int(rest[:i])
                
                if num == need:
                    if dfs(rest[i:], need - 1):
                        return True
            
            return False
        
        for i in range(1, len(s)):
            first = int(s[:i])
            rest = s[i:]
            
            if dfs(rest, first - 1):
                return True
        
        return False