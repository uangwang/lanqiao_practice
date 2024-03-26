n, m, k = map(int, input().split())


def check(x):
    # 第k小的数字mid,在原数组中小于等于mid的数字至少有k个
    ant = 0
    for i in range(1, n + 1):
        # 第i行的数字为：i,2i,3i,4i,...,mi
        # i*j <= x => j <= x // i
        # 第i行的数字中小于等于x的数字个数为min(m,x // i)
        ant += min(m,x // i)
    return ant >= k


left, right, ans = 1, n * m, 0
while left <= right:
    mid = (right + left) // 2
    if check(mid) >= k:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)
