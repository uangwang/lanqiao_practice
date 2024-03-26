"""
给定一个数x，将其拆分成n个正整数，后一个数要求大于等于前一个，给出方案
1.n重循环：n层树
2.DFS：从上往下找一条合法的路径（路径值不递减、长度为n。和为x）
"""

def dfs(depth,last_value):
    # depth表示当前在第几层
    # 递归出口
    if depth == n:
        # # 判断数字是否递增
        # for i in range(1,n):
        #     if path[i] >= path[i-1]:
        #         continue
        #     else:
        #         return # 不满足条件，直接返回
        # 判断和是否等于x
        if sum(path) != x:
            return
        print(path)
        return

        # 对于每一层，枚举当前拆出的数字
    for i in range(last_value, x + 1):
        path[depth] = i
        dfs(depth + 1, i)

x = int(input())
n = int(input())
path = [0] * n  # 表示第i个数字
dfs(0,1)
