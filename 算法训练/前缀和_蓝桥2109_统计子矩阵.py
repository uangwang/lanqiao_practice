n,m,k = map(int, input().split())
# 下标从一开始
a = [[0] * (m+1) for i in range(n+1)]
sum = [[0] * (m+1) for i in range(n+1)]

# 输入一个二维数组
for i in range(1,n+1):
    a[i] =[0] + list(map(int, input().split()))

# 求矩阵x1,y1到x2,y2的和
def get_sum(x1,y1,x2,y2):
    return sum[x2][y2] - sum[x1-1][y2] - sum[x2][y1-1] + sum[x1-1][y1-1]


# 预处理
for i in range(1,n+1):
    for j in range(1,m+1):
        sum[i][j] = sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1]+a[i][j]

    # 记录和不超过k的的矩阵数量
    ans = 0
    # 枚举左上角
    for x1 in range(1,n+1):
        for y1 in range(1,m+1):
            # 枚举右下角
            for x2 in range(x1,n+1):
                for y2 in range(y1,m+1):
                    if get_sum(x1,y1,x2,y2) <= k:
                        ans += 1
print(ans)
