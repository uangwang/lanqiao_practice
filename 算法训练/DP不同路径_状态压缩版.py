# 创建一个一维列表用于存储每列的唯一路径数
n,m = map(int,input().split())
dp = [1] * n

for j in range(1,m):
    for i in range(1,n):
        dp[i] += dp[i-1]

print(dp[n-1])