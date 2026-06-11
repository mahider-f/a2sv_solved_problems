class Solution:
    def __init__(self):
        self.dp={}
    def numTrees(self, n: int) -> int:
        res = 0
        if n <= 1:
            return 1
        
        if n in self.dp:
            return self.dp[n]
        for i in range(1, n+1):
            res += self.numTrees(i-1) * self.numTrees(n-i)
        
        self.dp[n] = res
        return res
        
        