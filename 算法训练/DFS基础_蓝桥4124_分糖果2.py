def dfs(depth):
    # depth 表示第几个小朋友
    # n 表示第一种糖果的剩余量
    # m 表示第二种糖果的剩余量

    # 当分完所有小朋友后，手上没有糖果
    if depth == 7:
        sum1, sum2 = 0, 0
        for i in range(7):
            sum1 += path[i][0]
            sum2 += path[i][1]
        if sum1 == 9 and sum2 == 16:
            global ans
            ans += 1
        return
    # 枚举当前小朋友的糖果可能性
    # 枚举第一种糖果
    for i in range(0,6):
        # 枚举第二种糖果
        for j in range(0,6):
            # 第depth个小朋友分到了i个第一种糖果，j个第二种糖果
            if 2<= i+j <=5 :
                path[depth][0] = i
                path[depth][1] = j
                dfs(depth+1)

ans = 0 # 记录答案，方案数
path = [[0,0] for i in range(7)]

dfs(0)
print(ans)