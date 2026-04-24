class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0] * len(graph) 

        def dfs(i, c):
            color[i] = c
            for n in graph[i]:
                if color[n] == c:
                    return False
                if color[n] == 0 and not dfs(n, -c):
                    return False
            return True

        for i in range(len(graph)):
            if color[i] == 0 and not dfs(i, 1):
                return False
        return True