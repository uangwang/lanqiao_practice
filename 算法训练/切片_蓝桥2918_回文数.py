ans = 0

for i in range(1, 10001):
    x = i

    for j in range(5):
        x += int(str(x)[::-1])

        if str(x)[::-1] == str(x):
            # 满足回文数
            break

    if j == 4 and str(x)[::-1] == str(x):
        # 五次操作仍是回文数
        ans += 1

print(ans)
