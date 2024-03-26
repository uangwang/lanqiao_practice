#确定矩阵大小
n = int(input())
#创建空矩阵
a = [[] for i in range(n)]
#金币初始化
for i in range(n):
    a[i] = list(map(int, input().split()))
#拿金币三种处理
for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            a[i][j] = a[i][j]
        elif i == 0:
            a[i][j] = a[i][j - 1] + a[i][j]
        elif j == 0:
            a[i][j] = a[i - 1][j] + a[i][j]
        else:
            a[i][j] = a[i][j] + max(a[i - 1][j], a[i][j - 1])
print(a[n - 1][n - 1])
