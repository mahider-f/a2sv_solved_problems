class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        root = list(range(n+1))

        def find(i):
            if root[i] != i:
                root[i] = find(root[i])
            else:
                root[i] = i
            return root[i]
        
        for x,y,_ in roads:
            root[find(x)] = find(y)
        res, g1 = float('inf'),find(1)

        for x, _,d in roads:
            if find(x) == g1:
                res = min(res,d)
        return res