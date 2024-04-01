n,x = map(int, input().split())
a = [0]+list(map(int, input().split()))
MOD = 998244353

# 原问题：给定n个正整数a,求有多少个子序列异或为x
# 子序列：子序列是从原序列中删除一些元素（可以一个元素都不删除，也可以删除所有元素）而不改变其余元素的相对顺序得到的序列
# 子问题：前i个正整数，有多少个子序列异或为j，方案数
# dp[i][j]表示前i个正整数，有多少个子序列异或为j，方案数
# 基于dp[0],dp[i-1] 如何求dp[i][j]？
# 第i个正整数：选择第i个数字，如何得到dp[i][j]？ =》 dp[i-1][j^a[i]]
# 第i个正整数：不选择第i个数字，如何得到dp[i][j]？ =》 dp[i-1][j]
# *** = j ^ a[i] =》 dp[i-1][j^a[i]]
# 状态转移方程：dp[i][j] = dp[i-1][j] + dp[i-1][j^a[i]]

# 初始化
dp =[[0] * 64 for _ in range(n+1)]
dp[0][0] = 1 # 一个都不选
for i in range(1,n+1):
    for j in range(64):
        dp[i][j] = (dp[i-1][j] + dp[i-1][j^a[i]]) % MOD

print(dp[n][x])

