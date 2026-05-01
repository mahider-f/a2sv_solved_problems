class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        adj = [[] for _ in range(len(bombs))]

        for i in range(len(bombs)):
            x1, y1, r1 = bombs[i]
            for j in range(i + 1, len(bombs)):
                x2, y2, r2 = bombs[j]
                d = (x1 - x2) ** 2 + (y1 - y2) ** 2

                if d <= r1 ** 2:
                    adj[i].append(j)
                if d <= r2 ** 2:
                    adj[j].append(i)

        def dfs(i, visit):
            if i in visit:
                return 0
            visit.add(i)
            for bomb in adj[i]:
                dfs(bomb, visit)
            return len(visit)

        res = 0
        for i in range(len(bombs)):
            res = max(res, dfs(i, set()))
        return res