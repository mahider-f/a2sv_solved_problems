from collections import deque
t = int(input())

for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    r = [x - 1 for x in r]

    indeg = [0] * n
    rev = [[] for _ in range(n)]

    for i, to in enumerate(r):
        indeg[to] += 1
        rev[to].append(i)

    q = deque(i for i in range(n) if indeg[i] == 0)
    removed = [False] * n

    while q:
        v = q.popleft()
        removed[v] = True

        to = r[v]
        indeg[to] -= 1
        if indeg[to] == 0:
            q.append(to)

    depth = [-1] * n
    q = deque()

    for i in range(n):
        if not removed[i]: 
            depth[i] = 0
            q.append(i)

    H = 0

    while q:
        v = q.popleft()

        for u in rev[v]:
            if depth[u] == -1:
                depth[u] = depth[v] + 1
                H = max(H, depth[u])
                q.append(u)

    print(H + 2)