def add_num(n):
    if n == 1:
        return 1
    ans = 1
    for i in range(1, n // 2 + 1):
        ans+=add_num(i)
        # print(n)
    return ans

if __name__ == '__main__':
    n = int(input())

    print(add_num(n))