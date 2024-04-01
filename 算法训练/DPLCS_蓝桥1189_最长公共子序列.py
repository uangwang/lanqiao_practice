N, M = map(int, input().split())
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))
print(a, b)
dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# 求出序列
res = []
i, j = N, M
while i > 0 and j > 0:
    # 从后往前找
    # 如果a[i] == b[j]，说明a[i]和b[j]是公共子序列的一部分
    if a[i] == b[j]:
        res.append(a[i])
        i -= 1
        j -= 1
    elif dp[i - 1][j] > dp[i][j - 1]: # 否则，如果dp[i-1][j] > dp[i][j-1]，说明dp[i][j]是由dp[i-1][j]转移过来的
        i -= 1
    else: # 否则，说明dp[i][j]是由dp[i][j-1]转移过来的
        j -= 1

print(res[::-1]) # 逆序输出

print(dp[N][M])
