import sys

input = sys.stdin.readline

n, m = map(int, input().split())

parent = list(range(n + 1))
size = [1] * (n + 1)
experience = [0] * (n + 1)
offset = [0] * (n + 1)


def find(x):
    if parent[x] != x:
        p = parent[x]
        parent[x] = find(p)
        offset[x] += offset[p]
    return parent[x]


def join(x, y):
    rx = find(x)
    ry = find(y)

    if rx == ry:
        return

    if size[rx] < size[ry]:
        rx, ry = ry, rx

    parent[ry] = rx
    offset[ry] = experience[ry] - experience[rx]
    size[rx] += size[ry]


def add(x, v):
    root = find(x)
    experience[root] += v


def get(x):
    root = find(x)
    return experience[root] + offset[x]


results = []

for _ in range(m):
    query = input().split()

    if query[0] == "join":
        join(int(query[1]), int(query[2]))

    elif query[0] == "add":
        add(int(query[1]), int(query[2]))

    else:
        results.append(str(get(int(query[1]))))

print("\n".join(results))