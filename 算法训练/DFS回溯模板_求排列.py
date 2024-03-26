def dfs(depth):
    # depth：第depth个数字
    if depth == n:
        print(path)
        return
    # 第depth个数字可以从1-n进行选择
    for i in range(1, n+1):
        # 选择的数字必须未标记
        if vis[i]:
            continue
        # 第depth选择了i
        vis[i] = True
        # 记录选择的数字
        path.append(i)
        # 递归到下一个数字
        dfs(depth+1)
        vis[i] = False
        path.pop(-1)

n = int(input())
vis = [False] * (n+1)
path = []
dfs(0)
