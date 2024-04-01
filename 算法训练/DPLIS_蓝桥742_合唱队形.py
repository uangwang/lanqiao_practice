# 最长上升子序列加最长下降子序列

N = int(input())
a = [0] + list(map(int, input().split()))
dp_up = [0] * (N + 1)
dp_down = [0] * (N + 1)

for i in range(1, N + 1):
    dp_up[i] = 1
    for j in range(1, i):
        if a[j] < a[i]:
            dp_up[i] = max(dp_up[i], dp_up[j] + 1)

# 最长下降子序列
# dp_down[i] = max(dp_down[j]) + 1, j > i, a[j] < a[i]
for i in range(N, 0, -1):
    dp_down[i] = 1
    for j in range(i + 1, N + 1):  # 从i+1到N
        if a[j] < a[i]:
            dp_down[i] = max(dp_down[i], dp_down[j] + 1)

ans = N - max([dp_up[i] + dp_down[i] - 1 for i in range(1, N + 1)])
print(ans)
