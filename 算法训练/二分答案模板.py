def check(mid):
    # 判断mid是否合法，合法返回True，否则返回False
    pass

left, right, ans = 初始化

while left <= right:
    mid = (left + right) // 2
    if check(mid):
        ans = mid
        left = mid + 1 # 或者right = mid - 1
    else:
        right = mid - 1 # 或者left = mid + 1
print(ans)