#dfs扩展能够到达的所有点
#从左往右，从上往下，对于每一个未标记的陆地，做一遍DFS
#DFS目的：扩展能够到达的所有点，并打上标记
#可以统计出有多少个连通块
def dfs(x,y):
    # 当前处于点x,y
    vis[x][y] = 1 # 标记为已走过

    # 判断当前点是否为高地
    if Map[x][y+1]=='#' and Map[x][y-1]=='#' and Map[x+1][y]=='#' and Map[x-1][y]=='#':
        global flag
        flag = True

    # 像四周扩展，把所有相邻的点打上标记
    for(delta_x,delta_y) in [(1,0),(0,1),(-1,0),(0,-1)]:
        new_x = x + delta_x
        new_y = y + delta_y
        if Map[new_x][new_y] == '#' and vis[new_x][new_y] == 0:
            dfs(new_x,new_y)


N = int(input())
Map = [list(input()) for _ in range(N)]
vis = [[0]*N for _ in range(N)] # 标记数组，标记是否走过
ans = 0 # 表示淹没岛屿的数量
for i in range(N):
    for j in range(N):
        if Map[i][j] =='#' and vis[i][j] == 0:
            # 先有一个标记flag，表示当前高地是否存在
            flag = False
            dfs(i,j)
            if flag == False:
                ans += 1
print(ans)