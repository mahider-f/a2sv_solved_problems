class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []

        def backtrack(n,path):
            
            if n == len(s):
                res.append(' '.join(path))
                return

            for i in range(n, len(s)):
                word = s[n:i+1]

                if word in wordDict:
                    path.append(word)
                    backtrack(i+1,path)
                    path.pop()
        backtrack(0,[])
        return res
            