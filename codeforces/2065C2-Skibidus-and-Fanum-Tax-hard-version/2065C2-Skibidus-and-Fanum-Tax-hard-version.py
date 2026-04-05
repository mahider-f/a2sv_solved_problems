from bisect import bisect_left,bisect_right
t = int(input())

for _ in range(t):
    n, m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    b.sort()

    prev = -float('inf')
    check = True
    
    for x in a:
        op1 = float('inf')
        op2 = float('inf')

        if x >= prev:
            op1 = x

        target = prev + x
        index = bisect_left(b,target)

        if index < m:
            op2 = b[index] - x
        best = min(op1,op2)

        if best == float('inf'):
            check = False
            break
        prev = best

    
    if check:
        print('YES')
    else:
        print("NO")