n = int(input())

act = [list(map(int,input().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]

dp[0][0] = act[0][0]
dp[0][1] = act[0][1]
dp[0][2] = act[0][2]

for i in range(1,n):
    dp[i][0] = act[i][0] + max(dp[i-1][1], dp[i-1][2])
    dp[i][1] = act[i][1] + max(dp[i-1][0], dp[i-1][2])
    dp[i][2] = act[i][2] + max(dp[i-1][0], dp[i-1][1])
print(max(dp[n-1]))