from functools import lru_cache
# 定义斐波那契
@lru_cache(None)
def fb(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fb(n-1) + fb(n-2)
num = 202202011200
# ans = (num // 60) * 8
# print('ans:',ans)
# s = 0
# # 斐波那契60一循环
# for i in range(1,num % 60 + 1):
#     if fb(i) % 10 == 7:
#         s+=1
# print('s:',s)
#
# ans_end = ans + s
# print(ans_end)
print((num//60)*8)
