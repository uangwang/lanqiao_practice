# 模拟只过了25%的数据
T = int(input())
for _ in range(T):
    n,m = map(int,input().split())
    flag = True
    for x in range(1,m+1):
        if not flag: # 如果已经找到了，就不用再找了
            break
        for y in range(x+1,m+1):
            # 取模
            if n % x == n % y:
                flag = False # 找到了
                print("Yes")
                break
    if flag: # 如果没有找到
        print("No")