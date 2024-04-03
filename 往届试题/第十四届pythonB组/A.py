"""2023"""


# 利用python的find函数
def find_i(i):
    find_1 = i.find('2')
    if find_1 == -1:
        return False
    find_2 = i.find('0', find_1 + 1)
    if find_2 == -1:
        return False
    find_3 = i.find('2', find_2 + 1)
    if find_3 == -1:
        return False
    find_4 = i.find('3', find_3 + 1)
    if find_4 == -1:
        return False
    return True


ans = 0
for i in range(12345678, 98765433):
    if find_i(str(i))==False:
        ans += 1
print(ans)
