# from datetime import datetime.timedelta
# # 常用的就是求两个日期中间间隔了多少天
# l = datetime(2002,6,1)
# r = datetime(2024.6.1)
# r-l # 默认显示天数，可以通过timedelta进行修改
#
# # 以及两个日期中间有多少个星期几什么的
# # 直接遍历
# delta = timedelta(days = 1)#
# while l != r:
#   l += delta


# from datetime import *
# start = date(1949,10,1)
# end = date(2012,10,1)
# ans = 0
# while start <= end:
#     if start.weekday()==6 and start.month==10 and start.day==1:
#         ans += 1
#     start += timedelta(1)
#
# print(ans)


# import datetime
#
# cnt = 0
# for i in range(1949,2013):
#   someday = datetime.datetime(year = i, month = 10, day = 1)
#   if someday.weekday() == 6:
#     cnt += 1
# print(cnt)

import calendar
cnt = 0
for i in range(1949,2013):
    if calendar.weekday(i,10,1) == 6:
        cnt += 1
print(cnt)

