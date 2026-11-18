class Solution:
    def minChanges(self, s: str) -> int:
        total = 0
        for i in range(0,len(s),2):
            if s[i]!= s[i+1]:
                total+=1
        return total
        