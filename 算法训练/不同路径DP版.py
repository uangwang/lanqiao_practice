# dp[i][j] 代表从（0，0）点到（i,j）点的不同路径数量
# dp[i][j] = dp[i-1][j] + dp[i][j-1]

n,m = map(int,input().split())

dp = [[0]*n for i in range(m)]

# n行m列，n看作y,m看作x

for i in range(m):
    dp[i][0] = 1
for j in range(n):
    dp[0][j] = 1

for i in range(1,m):
    for j in range(1,n):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        print(f'({i},{j}):{dp[i][j]}')

print(dp[m-1][n-1])

