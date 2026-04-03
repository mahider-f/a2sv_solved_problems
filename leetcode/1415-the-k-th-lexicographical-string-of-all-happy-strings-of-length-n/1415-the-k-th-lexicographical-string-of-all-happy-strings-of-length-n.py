class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        string = ['a','b','c']

        def backtrack(path):
            if len(res) == k:
                return
            if  len(path) == n:
                res.append(''.join(path[:]))
                return

            for x in string:
                if path and path[-1] == x:
                    continue
                path.append(x)
                backtrack(path)
                path.pop()
        res = []
        backtrack([])
        return res[k-1] if k <= len(res) else ""
