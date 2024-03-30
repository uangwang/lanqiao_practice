# 给定n种花，数量不超过ai,需要凑出m盆，求方案数
# 状态<i,j>：前i种花，数量为j盆的方案数，最终答案为dp[n][m]
# 状态转移：dp[i][j] = dp[i-1][j] + dp[i][j-1] + ...+dp[i-1][j-ai]
# 边界：dp[..][0] = 1
n, m = map(int, input().split())
a = list(map(int, input().split()))
MOD = 1000007
# 下标从1开始
dp = [[0] * (m+1) for i in range(n+1)]
# 边界
# 第i种花不选
for i in range(n+1):
    dp[i][0] = 1 # 一个都不选
for i in range(1, n+1):
    for j in range(1, m+1):
        # k是第i种花选的个数
        for k in range(min(a[i-1], j)+1): # 选0到a[i-1]个
            dp[i][j] += dp[i-1][j-k]
            dp[i][j] %= MOD
print(dp[n][m])
