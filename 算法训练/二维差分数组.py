def output(a,n):
    """输出一个二维矩阵"""
    for i in range(1,n+1):
        print(' '.join(map(str,a[i][1:])))

# n行m列的矩阵
n, m = map(int, input().split())

# 下标从一开始
a = [[0] * (m+1) for i in range(n+1)]
sum = [[0] * (m+1) for i in range(n+1)]
diff = [[0] * (m+1) for i in range(n+1)]

# 输入一个二维数组
for i in range(1,n+1):
    a[i] =[0] + list(map(int, input().split()))
output(a,n)

# 计算前缀和
for i in range(1,n+1):
    for j in range(1,m+1):
        sum[i][j] = sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1] + a[i][j]

# 计算二维差分数组
for i in range(1,n+1):
    for j in range(1,m+1):
        diff[i][j] = a[i][j] - a[i-1][j] - a[i][j-1] + a[i-1][j-1]

output(sum,n)
output(diff,n)