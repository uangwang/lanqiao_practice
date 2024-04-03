N,V = map(int,input().split())
dp = [[0] * (V+1) for _ in range(N+1)]
for i in range(1,N+1):
    wi,vi = map(int,input().split())
    for j in range(0,V+1):
        if j < wi:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-wi]+vi)
print(dp[N][V])

# 滚动数组版本
N,V = map(int,input().split())
dp = [0] * (V+1)
for i in range(1,N+1):
    wi,vi = map(int,input().split())
    # 从小到大，从wi到V，大于wi的情况不用考虑
    #01背包和完全背包的区别
    for j in range(wi,V+1):
        # 不放物品相当于不覆盖更新
        dp[j] = max(dp[j],dp[j-wi]+vi)
print(dp[V])
