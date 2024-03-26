def dfs(depth,n,m):
    # depth 表示第几个小朋友
    # n 表示第一种糖果的剩余量
    # m 表示第二种糖果的剩余量

    # 当分完所有小朋友后，手上没有糖果
    if depth == 7:
        if n == 0 and m == 0:
            global ans
            ans += 1
        return
    # 枚举当前小朋友的糖果可能性
    # 枚举第一种糖果
    for i in range(0,6):
        # 枚举第二种糖果
        for j in range(0,6):
            # 第depth个小朋友分到了i个第一种糖果，j个第二种糖果
            if 2<= i+j <=5 and n-i >= 0 and m-j >= 0:
                dfs(depth+1,n-i,m-j)


ans = 0 # 记录答案，方案数


dfs(0,9,16)
print(ans)