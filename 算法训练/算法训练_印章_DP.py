#创建二维数组
n,m = map(int,input().split())
#数组初始化为0
dp = [[0 for i in range(n+1)] for j in range(m+1)]

for i in range(1,m+1):
    for j in range(1,n+1):
        if i < j:
            dp[i][j] = 0
        elif i == 1:
            dp[i][j] = pow(1/n, i-1)
        else:
            dp[i][j] = dp[i-1][j] * (1/n) * j + dp[i-1][j-1] * (1/n) * (n-(j-1))

print("{:.4f}".format(dp[m][n]))
