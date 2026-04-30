class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indeg = [0 for _ in range(n+1)]
        adj = [[] for _ in range(n+1)]
        max_time = [0 for _ in range(n+1)]
        queue = deque()
        
        for crs, pre in relations:
            adj[crs].append(pre)
            indeg[pre] += 1
        for i in range(1, n+1):
            if indeg[i] == 0:
                queue.append(i)
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                max_time[node] += time[node-1]

                for child in adj[node]:
                    indeg[child] -=1
                    if indeg[child] == 0:
                        queue.append(child)
                    max_time[child] = max(max_time[node], max_time[child])
        return max(max_time)