class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        source = 0
        dest = len(graph) - 1

        def dfs(node,path):
            if path and path[-1] == dest:
                ans.append(path[:])
                return

            for n in graph[node]:
                path.append(n)
                dfs(n,path)
                path.pop()

        dfs(0,[0])
        return ans