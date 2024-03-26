L,N,M = map(int,input().split())
a = []
for i in range(N):
    a.append(int(input()))

def check(x):
    """
    假设最短跳跃距离为x,移除的岩石数量不超过M，则为合法
    :param x:
    :return:
    """
    # 移除的岩石数量
    cnt = 0
    # 上一个岩石的位置
    pre = 0
    # 从小岩石到大岩石，判断是否能移除
    for i in range(N):
        if a[i] - pre >= x:
            pre = a[i]
        else:
            cnt += 1
    if L - pre < x:
        return False
    return cnt <= M


left, right = 1,L
ans = -1
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1
print(ans)