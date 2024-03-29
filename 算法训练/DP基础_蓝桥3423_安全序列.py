# dp[i]表示前i个位置的方案数
"""
状态转移考虑两种：
1.不放置：从dp[i-1]转移过来
2.放置：从dp[i-k-1]转移过来
"""
# 状态转移方程：dp[i] = dp[i-1] + (dp[i-k-1] if (i-k-1)>=0 else 1)
MOD = 1000000007
n, k = map(int, input().split())
dp = [0] * (n+1)

# 初始状态，不放置也是一种方案
dp[0] = 1
for i in range(1, n+1):
    # 状态转移
    # 放置：从dp[i-k-1]转移过来
    # 不放置：从dp[i-1]转移过来
    dp[i] = (dp[i-1] + (dp[i-k-1] if (i-k-1)>=0 else 1)) % MOD
print(dp[n])