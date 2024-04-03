# count的使用
# count() 方法用于统计某个元素在列表中出现的次数。
# list.count(obj)
# 参数
# obj -- 列表中统计的对象。
# 返回值
# 返回元素在列表中出现的次数。
# 示例
list1 = ['Google', 'Runoob', 'Taobao', 'Google']
list1.count('Google')  # 2
list1.count('Runoob')  # 1
list1.count('Taobao')  # 1
list1.count('Baidu')  # 0
list1.count('Google')  # 1
#
# index的使用
# index() 方法用于从列表中找出某个值第一个匹配项的索引位置。
# list.index(x[, start[, end]])
# 参数
# x -- 查找的对象。
# start -- 可选，查找的起始位置。
# end -- 可选，查找的结束位置。
# 返回值

# 示例
list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list1.index('Taobao')  # 2