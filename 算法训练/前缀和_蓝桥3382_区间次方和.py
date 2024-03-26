# MOD = 10000000007
# def get_presum(a,k):
#     n = len(a)
#     sum = [0] * n
#     sum[0] = a[0]**k
#     for i in range(1,n):
#         sum[i] = sum[i-1] + a[i]**k
#     sum = [i % MOD for i in sum]
#     return sum
#
# def get_sum(l,r,sum):
#     if l ==0:
#         return sum[r]
#     else:
#         return (sum[r] - sum[l-1] + MOD) % MOD
#
# n,m = map(int, input().split())
# a = list(map(int, input().split()))
# # 每行输入三个整数l,r,k表示一个查询
# for _ in range(m):
#     l,r,k = map(int, input().split())
#     sum = get_presum(a,k)
#     # 答案对10^9+7取模
#     print(get_sum(l,r,sum) % (10**9+7))
from itertools import accumulate

MOD = 10000000007
def get_presum(a):
    sum = list(accumulate(a))
    sum = [i % MOD for i in sum]
    return sum

def get_sum(l,r,sum):
    if l ==0:
        return sum[r]
    else:
        return (sum[r] - sum[l-1] + MOD) % MOD

n,m = map(int, input().split())
a = list(map(int, input().split()))

sum_list = []
for i in range(1,6):
    tmp_a = [x**i for x in a]
    sum_list.append(get_presum(tmp_a))

for _ in range(m):
    l,r,k = map(int, input().split())
    print(get_sum(l-1,r-1,sum_list[k-1]))