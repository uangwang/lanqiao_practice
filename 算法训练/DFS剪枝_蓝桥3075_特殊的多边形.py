# 利用DFS求所有的N边形，边长乘积不超过100000

def dfs(depth, last_val, tot, mul):
    """
    :param depth: 第几条边
    :param last_val: 上一条边的长度
    :param tot: 当前边长之和
    :param mul: 当前边长之积
    :return:
    """
    if depth == n:
        if tot > 2 * path[-1]:
        # 此时是一个合法的N边形
            ans[mul] += 1
        return
    # 枚举第depth条边的长度为i
    for i in range(last_val + 1, 100000):
        # 剪枝，保证乘积不超过100000
        # 先前选择了depth个数字，乘积为mul,
        # 后续还有n-depth个数字，每个数字都要 >= i
        if mul * (i ** (n - depth)) > 100000:
            break
        path.append(i)
        dfs(depth + 1, i, tot + i, mul * i)
        path.pop()

# ans[i]表示价值为i的N变形的数量
ans = [0]*100001
t, n = map(int, input().split())
path = []
dfs(0, 0, 0, 1)
# 每次询问一个区间[l,r]，输出有多少个N边形的价值在这个区间内
# 等价于ans[l]+ans[l+1]+...+ans[r],所以需要对ans求前缀和
for i in range(100001):
    ans[i] += ans[i-1]
for _ in range(t):
    l, r = map(int, input().split())
    print(ans[r]-ans[l-1])
