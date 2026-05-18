n, m, k = map(int, input().split())


for _ in range(m):
    input()

tasks = []

for _ in range(k):
    t, u, v = input().split()
    tasks.append((t, int(u), int(v)))

parent = list(range(n + 1))
size = [1] * (n + 1)


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    if size[a] < size[b]:
        a, b = b, a

    parent[b] = a
    size[a] += size[b]


ans = []


for t, u, v in reversed(tasks):

    if t == "ask":
        if find(u) == find(v):
            ans.append("YES")
        else:
            ans.append("NO")

    else:  
        union(u, v)


ans.reverse()

for i in ans:
    print(i)