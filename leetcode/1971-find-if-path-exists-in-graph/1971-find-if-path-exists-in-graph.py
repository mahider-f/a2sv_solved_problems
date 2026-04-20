class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph = [[] for _ in range(n)]

        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        visited = [False for _ in range(n)]
        def dfs(vertex):
            if vertex == destination:
                return True

            visited[vertex] = True
            found = False

            for neighbour in graph[vertex]:
                if not visited[neighbour]:
                    found = dfs(neighbour)

                if found:
                    return True
            return False

        return dfs(source)


            