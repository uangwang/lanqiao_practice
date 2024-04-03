# N,V = map(int,input().split())
# dp = [[0] * (V+1) for _ in range(N+1)]
# for i in range(1,N+1):
#     wi,vi = map(int,input().split())
#     for j in range(0,V+1):
#         if j < wi:
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = max(dp[i-1][j],dp[i-1][j-wi]+vi)
# print(dp[N][V])

# 滚动数组版本
# N,V = map(int,input().split())
# dp = [[0] * (V+1) for _ in range(2)]
# for i in range(1,N+1):
#     wi,vi = map(int,input().split())
#     for j in range(0,V+1):
#         if j < wi:
#             dp[i%2][j] = dp[(i-1)%2][j]
#         else:
#             dp[i%2][j] = max(dp[(i-1)%2][j],dp[(i-1)%2][j-wi]+vi)
# print(dp[N%2][V])

# 优化空间复杂度
N,V = map(int,input().split())
dp = [0] * (V+1)
for i in range(1,N+1):
    wi,vi = map(int,input().split())
    # 必须从大到小，从V到wi，小于wi的情况不用考虑
    for j in range(V,wi-1,-1):
        # 不放物品相当于不覆盖更新
        dp[j] = max(dp[j],dp[j-wi]+vi)
print(dp[V])