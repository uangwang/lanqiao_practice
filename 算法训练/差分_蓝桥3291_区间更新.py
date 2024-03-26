# 运用于若干组数据
while True:
    try:
        n,m = map(int, input().split())
        a = list(map(int, input().split()))
        # 定义差分数组
        diff = [0] * (n+1)
        diff[0] = a[0]
        for i in range(1,n):
            diff[i] = a[i] - a[i-1]
        # 处理m次操作，每次对[l,r]区间加c
        for _ in range(m):
            l,r,c = map(int, input().split())
            l -= 1
            r -= 1
            diff[l] += c
            diff[r+1] -= c

        # 将查分数组还原为原数组
        a[0] = diff[0]
        for i in range(1,n):
            a[i] = diff[i] + a[i-1]
        print(' '.join(map(str,a)))




    except:
        break