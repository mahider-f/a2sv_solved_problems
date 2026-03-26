class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ''

        Set = set(s)

        for i,c in enumerate(s):
            if c.swapcase() not in Set:
                s1 = self.longestNiceSubstring(s[:i])
                s2 = self.longestNiceSubstring(s[i+1:])
                return s2 if len(s2) > len(s1) else s1
        return s
        