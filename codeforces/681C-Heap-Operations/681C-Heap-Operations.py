import heapq

n = int(input())

heap = []
ans = []

for _ in range(n):
    op = input().split()

    if op[0] == "insert":
        x = int(op[1])
        heapq.heappush(heap, x)
        ans.append(f"insert {x}")

    elif op[0] == "removeMin":
        if not heap:
            heapq.heappush(heap, 0)
            ans.append("insert 0")

        heapq.heappop(heap)
        ans.append("removeMin")

    else:  
        x = int(op[1])

        while heap and heap[0] < x:
            heapq.heappop(heap)
            ans.append("removeMin")

        if not heap or heap[0] > x:
            heapq.heappush(heap, x)
            ans.append(f"insert {x}")

        ans.append(f"getMin {x}")

print(len(ans))
for a in ans:
    print(a)