s1 = list(input())
s2 = list(input())
n = len(s1)
ans = 0
for i in range(n):
    if s1[i] == s2[i]:
        continue
    else:
        if s1[i + 1] == '*':
            s1[i + 1] = 'o'
        else:
            s1[i + 1] = '*'
    ans += 1
print(ans)