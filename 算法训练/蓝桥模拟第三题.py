n,q = map(int,input().split())
s = [0] + [ord(ch) for ch in input()]
diff = [0] * (n+2)
diff[0] = s[0]
for i in range(1,n+1):
    diff[i] = s[i] - s[i-1]

for _ in range(q):
    l,r,k = map(int,input().split())
    diff[l] += k
    diff[r+1] -= k

for i in range(1,n+1):
    s[i] = diff[i] + s[i-1]
    print(chr(s[i]),end='')