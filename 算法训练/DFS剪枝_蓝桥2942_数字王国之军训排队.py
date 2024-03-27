def check(x,group):
    # 判断学生x能否加入group组
    for y in group:
        if x % y == 0 or y % x == 0:
            return False
    return True


def dfs(depth):
    # 最优性剪枝
    if len(Group) >= ans:
        return
    # depth：当前是第几个学生
    # 递归出口
    if depth == n:
        global ans
        ans = min(ans, len(Group))
        return

    # 对于每个学生，枚举该学生放在哪一组
    for every_group in Group:
        # 当前第depth个学生能否加入当前组
        # 可行性剪枝
        if check(a[depth], every_group):
            every_group.append(a[depth])
            dfs(depth+1)# 递归
            every_group.pop()# 回溯

    # 对于每个学生，也可以单独作为一个组
    Group.append([a[depth]])
    dfs(depth+1)
    Group.pop()

n = int(input())
a = list(map(int, input().split()))
# Group表示分组情况，每个元素表示一个组内的情况
Group = []
ans = n
dfs(0)
print(ans)