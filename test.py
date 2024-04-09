import os
import sys

# 请在此输入您的代码
n , B = map(int,input().split())
li = list(map(int,input().split()))
cnt=0
res = []
for i in range(n-1):
  if li[i] % 2 == 0:
    cnt += 1
  else:
    cnt -= 1
  if cnt ==0:
    res.append(abs(li[i+1]-li[i]))

res.sort()
ans = 0
for i in res:
  if B >= i:
    ans += 1
    B -= i
  else:
    break

print(ans)