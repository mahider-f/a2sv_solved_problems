class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        ans = []

        for src,dst in edges:
            adj[dst].append(src)
        
        def dfs(node,path):
            for parent in adj[node]:
                if parent not in path:
                    path.add(parent)
                    dfs(parent,path)
            
        for i in range(n):
            ancestor = set()
            dfs(i,ancestor)

            ans.append(list(sorted(ancestor)))
        return ans