n, m = map(int, input().split())
a = []
b = [[0] * m for i in range(n)]

# 使用列表生成式初始化 a
for i in range(n):
    a.append(list(map(int, input().split())))

dir = [(0, 1), (0, -1), (-1, 0), (1, 0), (-1, 1), (1, 1), (1, -1), (-1, -1), (0, 0)]

for i in range(n):
    for j in range(m):
        cnt, tot = 0, 0
        # for k in range(8):
        #     x, y = i + dir[k][0], j + dir[k][1]
        for delta_x in [-1, 0, 1]:
            for delta_y in [-1, 0, 1]:
                x, y = i + delta_x, j + delta_y
                if 0 <= x < n and 0 <= y < m:
                    tot += a[x][y]
                    cnt += 1
        b[i][j] = tot // cnt


