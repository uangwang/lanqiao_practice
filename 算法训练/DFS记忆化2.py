from functools import lru_cache
@lru_cache(maxsize=None)
def f(x):
    if x == 1 or x == 2:
        return 1
    return f(x - 1) + f(x - 2)

n = int(input())
print(f(n) % 100000007)
