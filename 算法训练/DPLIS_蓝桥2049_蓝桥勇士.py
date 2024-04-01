n = int(input())
a = [0] + list(map(int, input().split()))

dp = [0] * (n+1)

for i in range(1,n+1):
    # 更新dp[i]
    dp[i] = 1 # 至少包含自己
    for j in range(1,i):
        # 在i的前面找到小于a[i]的数字a[j]
        # 用对应的dp[j]更新dp[i]
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))