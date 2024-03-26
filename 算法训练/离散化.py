# import二分查找
from bisect import bisect_left
def Discrete(a):
    """

    :param a: 输入列表a
    :return: 返回离散化数组
    """
    # 1.拷贝一份b，排序去重
    b=list(set(a))
    b.sort()
    print(b)
    ans = []
    # 2.对a中的每个元素，将x转换成b列表的下标
    for x in a:
        ans.append(bisect_left(b,x)+1)
    return ans

# 构建字典
def Discrete_dict(a):
    """

    :param a: 输入列表a
    :return: 返回离散化数组
    """
    # 1.拷贝一份b，排序去重
    b=list(set(a))
    b.sort()
    print(b)

    dic = dict(zip(b,list(range(len(b)))))

    ans = []
    # 2.对a中的每个元素，将x转换成b列表的下标
    for x in a:
        ans.append(dic[x]+1)
    return ans

if __name__ == '__main__':
    a = list(map(int, input().split()))
    print(Discrete(a))
    print(Discrete_dict(a))