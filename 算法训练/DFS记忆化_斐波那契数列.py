import sys
sys.setrecursionlimit(1000000)
dic = {0:1,1:1}
def dfs(n):
    if n in dic.keys():
        return dic[n]
    dic[n] =(dfs(n-1)+dfs(n-2)) % 100000007
    return dic[n]

n = int(input())
print(dfs(n))