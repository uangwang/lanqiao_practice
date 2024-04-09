obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# m行n列
m = len(obstacleGrid)
n = len(obstacleGrid[0])
if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
    print(0)


dp= [[0] * n for _ in range(m)]

for i in range(m):
    if obstacleGrid[i][0] == 0:
        dp[i][0] = 1
    else:
        break
for j in range(n):
    if obstacleGrid[0][j] == 0:
        dp[0][j] = 1
    else:
        break

for i in range(1,m):
    for j in range(1,n):
        if obstacleGrid[i][j] == 1:
            continue
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
        print(dp[i][j])

print(dp[m-1][n-1])
