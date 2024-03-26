left, right = 1, 2
eps = 1e-6
while right - left > eps:
    mid = (left + right) / 2
    if mid * mid > 2:
        right = mid
    else:
        left = mid
    print(left, right)
