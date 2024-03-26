def dfs(depth,weight,cnt):
    # depth：第depth个瓜
    # weight：当前买到的瓜的重量
    # cnt: 当前砍了几次
    if weight>m:
        # 如果当前重量超过了m，直接返回
        return
    if weight==m:
        # 如果当前重量等于m，输出答案
        global ans
        ans = min(ans,cnt)
    if depth==n:
        return

    # 枚举当前瓜的三种情况
    # 1.不买
    dfs(depth+1,weight+0,cnt)
    # 2.买一半
    dfs(depth+1,weight+A[depth]//2,cnt+1)
    # 3.买整个
    dfs(depth+1,weight+A[depth],cnt)


n,m = map(int,input().split())
m = m*2
A = list(map(int,input().split()))
A = [ x * 2 for x in A]
ans = n+1
dfs(0,0,0)
if ans == n+1:
    print(-1)
else:
    print(ans)
