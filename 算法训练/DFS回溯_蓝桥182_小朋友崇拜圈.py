import sys
sys.setrecursionlimit(1000000)
# 当前位于点x，步长为length
def dfs(x,length):
    # 记录走到x的步长为length
    vis[x] = length

    # 接下来要走下一个点
    # 判断下一个点是否走过
    if vis[a[x]] == 0:
        # 如果没有走过，就继续走下去
        dfs(a[x],length+1)
    else:
        # 如果走过了，就说明形成了环，就要计算环的长度
        global ans
        ans = max(ans,length-vis[a[x]]+1)
        return


n = int(input())
a = [0]+list(map(int, input().split()))
# 标记数组：vis[x]表示点x的步数
vis = [0]*(n+1)
ans = 0

for i in range(1,n+1):
    if vis[i] == 0:
        dfs(i,1)

print(ans)