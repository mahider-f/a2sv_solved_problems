n, k = map(int,input().split())

stones = list(map(int,input().split()))
memo = [float('inf')]*n
memo[0] = 0

for i in range(1,n):
    for j in range(k+1):
        if i - j >= 0:
            memo[i] = min(memo[i], memo[i-j]+abs(stones[i]- stones[i-j]))
    
print (memo[n-1])