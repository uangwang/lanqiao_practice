n,S = map(int, input().split())
a = list(map(int, input().split()))
n = len(a)
min_len = n+1
tot = 0
# 快慢指针找最短区间
slow,fast = 0,0
while slow < n:
    while fast < n and tot < S:
        tot += a[fast]
        fast += 1
    if tot >= S:
        min_len = min(min_len,fast-slow)

    # 开始针对左端点进行变化
    tot -= a[slow]
    slow += 1
print(min_len if min_len != n+1 else 0)