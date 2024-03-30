# 下标从1开始
N = int(input())
a = [[0]*(N+1)]
for i in range(N):
    a.append([0]+list(map(int, input().split())))

# <i,j>表示从(i,j)出发到底部的最大和
# 最终答案 = dp[0][0]
# (i,j)可以向下走到(i+1,j)或(i+1,j+1)
# dp[i][j] = a[i][j] + max(dp[i+1][j], dp[i+1][j+1])

dp = [[0] * (N+1) for _ in range(N+1)]
# 更新需要从下往上更新：从n-1到0
for i in range(N, 0, -1):
    # 枚举第i行的每一个元素，第i行有i个元素
    for j in range(1,i+1):
        # 最后一行的元素就是自己
        if i == N:
            dp[i][j] = a[i][j]
        else:
            dp[i][j] = a[i][j] + max(dp[i+1][j], dp[i+1][j+1])

print(dp[1][1])