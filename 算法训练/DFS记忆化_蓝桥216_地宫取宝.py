from functools import lru_cache
@lru_cache(None)
def dfs(x, y, z, w):
    """
    :param x: 当前横坐标
    :param y: 当前纵坐标
    :param z: 先前拿的宝物数量
    :param w: 先前拿的宝物的最大价值
    :return: 从当前状态出发的方案数
    """
    # 递归出口
    if x == n-1 and y == m-1:
        if z == k:
            return 1
        if z == k-1 and w < Map[x][y]:
            return 1
        return 0

    # 两个方向，朝右，朝下
    # 方案数 = 朝右的方案数 + 朝下的方案数
    ans = 0
    for delta_x, delta_y in [(0, 1), (1, 0)]:
        new_x,new_y = x+delta_x,y+delta_y
        if new_x < n and new_y < m:
            # 当前不选择宝物，走到（new_x, new_y）的方案数
            ans += dfs(new_x, new_y, z, w)
            # 当前选择宝物，走到（new_x, new_y）的方案数
            if w < Map[x][y]:
                ans += dfs(new_x, new_y, z+1, Map[x][y])
            ans %= 1000000007
    return ans


n, m, k = map(int, input().split())
Map = []
for i in range(n):
    Map.append(list(map(int, input().split())))

print(dfs(0, 0, 0, -1))
