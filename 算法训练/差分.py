# 差分数组
N,Q = map(int,input().split())
s = [0] + [ord(ch) - 97 for ch in input()]


# 定义差分数组
diff = [0] * (N + 2)
diff[0] = s[0]
for i in range(1,N+1):
    diff[i] = s[i] - s[i-1]

# 处理Q次操作
for _ in range(Q):
    l,r,k = map(int,input().split())
    k = k % 26
    diff[l] += k
    diff[r+1] -= k

for i in range(1,N+1):
    s[i] = diff[i] + s[i-1]
    print(chr(s[i]%26+97),end='')