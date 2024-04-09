from functools import lru_cache


@lru_cache(None)
def dfs(x, y, j, k):
    if x > j or y > k:
        return 0
    if x == j and y == k:
        return 1
    return dfs(x + 1, y, j, k) + dfs(x, y + 1, j, k)