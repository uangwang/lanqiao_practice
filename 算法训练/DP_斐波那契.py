# 状态压缩
n = int(input())
if n <= 1:
    print(n)

dp = [0,0]
dp[0] = 0
dp[1] = 1

for i in range(2,n+1):
    sum = dp[0] + dp[1]
    dp[0] = dp[1]
    dp[1] = sum

print(dp[1])

# 普通形式
n = int(input())
dp = [0] * (n+1)
dp[0] = 0
dp[1] = 1
for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])

# 版本三
n = int(input())
if n <= 1:
    print(n)

prev1,prev2 = 0,1
for _ in range(2,n+1):
    curr = prev1 + prev2
    prev1,prev2 = prev2,curr

print(prev2)