from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

adj = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)


def bfs(start):
    dist = [-1] * (n + 1)

    q = deque([start])
    dist[start] = 0

    while q:
        node = q.popleft()

        for nei in adj[node]:
            if dist[nei] == -1:
                dist[nei] = dist[node] + 1
                q.append(nei)

    farthest_node = start
    max_dist = 0

    for i in range(1, n + 1):
        if dist[i] > max_dist:
            max_dist = dist[i]
            farthest_node = i

    return farthest_node, max_dist



a, _ = bfs(1)

b, diameter = bfs(a)

print(diameter * 3)