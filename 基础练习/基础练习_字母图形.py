n,m = list(map(int,input().split()))
zimu = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# print(n)
# print(m)

for i in range(n):
    behind_str = zimu[:m]
    front_str = zimu[1:i+1]
    result = front_str[::-1] + behind_str
    print(result[0:m])
