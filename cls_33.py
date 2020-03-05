# !/usr/bin/python
# coding: utf8
# Time: 2020/3/5 16:41
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import time

# t0 = time.perf_counter()
# t1 = time.process_time()
# sum = 0
# for i in range(900000):
#     sum += i
# print('cost:', time.perf_counter()-t0)
# print('cost:', time.process_time()-t1)

# print(time.asctime())
# time.sleep(5)
# print(time.asctime())

"""计算2000年4月1日到2018年4月1日一共有多少个闰年，如果是闰年的话把父亲节
   的日期打印出来。（父亲节是每年六月的第三个星期日）
"""
import calendar


# print(calendar.month(2019, 4))
# print(calendar.calendar(2020))


def find_father_day(year):
    times = 0
    for day in range(1, 31):
        if calendar.weekday(year, 6, day) == 6:
            times += 1
        if times == 3:
            print("The Father's day of {} is {}.6.{}".format(year, year, day))
            break

"""
number_of_leap = calendar.leapdays(2000, 2018)
print("一共有{}个闰年".format(number_of_leap))
for y in range(2000, 2019):
    if calendar.isleap(y):
        find_father_day(y)
"""

# 你出生的那一天星期几？
# print("我出生的那一天是星期{}".format(calendar.weekday(1997, 2, 20)+1))

import datetime
print(datetime.date(1997, 2, 20) + datetime.timedelta(days=10000))  # 你出生后10000天的日期是什么？

d0 = datetime.date(1997, 2, 20)
# d1 = datetime.date(2020, 3, 5)
d1 = datetime.datetime.now().date()

print(d1-d0)  # 从出生到今天为止

