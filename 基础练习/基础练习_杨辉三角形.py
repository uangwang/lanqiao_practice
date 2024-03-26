n = int(input())

arr = [[0] * n for i in range(n)]

for line in range(n):
    for i in range(n):
        if i==0:
            arr[line][i] = 1
        else:
            arr[line][i] = arr[line-1][i-1] + arr[line-1][i]

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            print(arr[i][j],end=" ")
    print()
        
        
