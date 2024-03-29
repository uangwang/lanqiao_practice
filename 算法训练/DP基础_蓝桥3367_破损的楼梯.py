import os
import sys


# 动态规划解法
def dp(N, vis):
    MOD = 1000000007
    if N == 0:
        return 1
    if N == 1:
        return 1 - vis[1]

    # 初始化DP数组
    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 1 - vis[1]

    # 动态规划计算
    for i in range(2, N + 1):
        if vis[i]:
            dp[i] = 0
        else:
            dp[i] = (dp[i - 1] + dp[i - 2]) % MOD

    return dp[N]


N, M = map(int, input().split())
a = list(map(int, input().split()))
vis = [0] * (N + 1)
for x in a:
    vis[x] = 1

print(dp(N, vis))
