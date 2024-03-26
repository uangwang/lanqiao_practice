n,m,k = map(int,input().split())
a = list(map(int,input().split()))
left,right = 0,0
cnt = 0
ans = 0
while left < n:
    while right < n and cnt < k:
        if a[right] >= m:
            cnt += 1
        right += 1
    if cnt >= k:
        ans += n - right + 1
    if a[left] >= m:
        cnt -= 1
    left += 1
print(ans)