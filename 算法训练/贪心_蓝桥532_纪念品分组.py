w = int(input()) # 每组纪念品价格之和的上限
n = int(input()) # 纪念品的数量
a =[]
while True:
    try:
        a.append(int(input()))
    except:
        break
# print(a)
a.sort()
ans = 0
l,r = 0, n-1
while l <= r:
    if a[l] + a[r] <= w:
        ans += 1
        l += 1
        r -= 1
    else:
        r -= 1
        ans += 1
print(ans)
