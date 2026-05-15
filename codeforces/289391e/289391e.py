import heapq
n, m = map(int,input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    u,v,w = map(int,input().split())
    adj[u].append((v,w))
    adj[v].append((u,w))

heap = []
visited = [False]*(n+1)
ans = 0

heapq.heappush(heap,(0,1))

while heap:
    wt, u = heapq.heappop(heap)

    if visited[u]:
        continue
    ans += wt
    visited[u] = True

    for v in adj[u]:
        if not visited[v[0]]:
            heapq.heappush(heap, (v[1],v[0]))
print (ans)