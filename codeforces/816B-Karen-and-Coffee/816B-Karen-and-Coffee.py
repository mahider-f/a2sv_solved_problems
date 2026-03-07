n, k , q = map(int, input().split())
max_ = 200000
prefix = [0]*(max_+2)

for _ in range(n):
    l, r = map(int, input().split())
    prefix[l] +=1
    prefix[r+1] -=1

for i in range(1,max_+1):
    prefix[i] += prefix[i-1]

good = [0]*(max_+2)
for i in range(1, max_+1):
    if prefix[i] >= k:
        good[i] = 1

for i in range(1, max_+1):
    good[i] += good[i-1]

for _ in range(q):
    a, b = map(int, input().split())
    print(good[b] - good[a-1])