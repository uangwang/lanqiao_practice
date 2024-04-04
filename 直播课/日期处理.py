from datetime import datetime.timedelta
# 常用的就是求两个日期中间间隔了多少天
l = datetime(2002,6,1)
r = datetime(2024.6.1)
r-l # 默认显示天数，可以通过timedelta进行修改

# 以及两个日期中间有多少个星期几什么的
# 直接遍历
delta = timedelta(days = 1)#
while l != r:
  l += delta
