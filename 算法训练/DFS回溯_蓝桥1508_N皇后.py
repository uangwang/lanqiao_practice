def dfs(x):
    # 第x层皇后
    if x == n+1:
        global ans
        ans += 1
        return

    # 第x层的皇后枚举每一列
    for y in range(1,n+1):  # 这里应该是n+1，因为range函数是左闭右开的
        # 当前的坐标为(x,y)，要求当前列，当前主副对角线不能被攻击到
        if vis1[y] is False and vis2[x+y] is False and vis3[x-y+n] is False:
            # 此时可以放置皇后
            vis1[y] = vis2[x+y] = vis3[x-y+n] = True
            dfs(x+1)
            # 回溯 恢复现场，标记清空
            vis1[y] = vis2[x+y] = vis3[x-y+n] = False
        else:
            continue

n = int(input())
# 三个数组分别表示列、主对角线、副对角线是否被标记
vis1= [False] * (n+1)
vis2 = [False] * (2*n+1)
vis3 = [False] * (2*n+1)
ans = 0
dfs(1)
print(ans)