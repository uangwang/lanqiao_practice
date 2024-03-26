N,K = map(int,input().split())
a = []
for i in range(N):
    Hi, Wi = map(int,input().split())
    a.append((Hi,Wi))

# 合法：假定切出的巧克力边长为x,能否切出k块
def check(x):
    # cnt表示切出的巧克力块数
    cnt = 0
    for H,W in a:
        # 一行能切出的巧克力块数
        cnt += (H // x) * (W // x)
        if cnt >= K:
            return True
    return False

# 边长搜索区间
left, right = 1, 10**5
ans = 1
while left <= right:
    mid = (left + right) // 2
    if check(mid ):
        ans = mid
        # 求最大值 [mid+1, right]
        left = mid + 1
    else:
        # 求最小值 [left, mid-1]
        right = mid - 1
print(ans)