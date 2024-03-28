from functools import lru_cache
@lru_cache(None)
def dfs(x,y,z):
    # 坐标为(x,y),z表示是否使用过背包
    # 能够逃离就返回True，否则返回False
    if x == C and y == D:
        return True

    # 如果没走到终点，就四个方向判断
    for delta_x,delta_y in [(0,1),(0,-1),(1,0),(-1,0)]:
        new_x,new_y = x+delta_x,y+delta_y
        # 判断新坐标是否越界
        if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
            continue
        # 如果新坐标比旧坐标低，就可以走到新坐标
        if Map[new_x][new_y] < Map[x][y]:
            if dfs(new_x,new_y,z):
                return True
        # 如果新坐标比旧坐标高，就需要判断是否使用背包
        elif Map[new_x][new_y]<Map[x][y] + k and z == False:
            if dfs(new_x,new_y,True):
                return True

# n,m表示坐标范围，k表示使用一次性喷气背包可以升高的高度
n,m,k = map(int,input().split())
# A,B表示起始坐标，C,D表示目标坐标
A,B,C,D = map(int,input().split())
# 下标从0开始，所以坐标要减1
A,B,C,D = A-1,B-1,C-1,D-1
# 初始化地图
# Map表示每个点的高度
Map = []
for i in range(n):
    Map.append(list(map(int,input().split())))
if dfs(A,B,False):
    print("YES")
else:
    print("NO")