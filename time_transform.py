# coding=utf-8
# Version 1.1.2
import time

weekdict = {"Monday": "星期一", "Tuesday": "星期二", "Wednesday": "星期三",
            "Thursday": "星期四", "Friday": "星期五", "Saturday": "星期六", "Sunday": "星期天"}
monthdict = {"January": "一月", "February": "二月", "March": "三月", "April": "四月", "May": "五月", "June": "六月",
             "July": "七月", "August": "八月", "September": "九月", "October": "十月", "November": "十一月", "December": "十二月"}

def timestr(t:str) -> str:
    return time.strftime(t, time.localtime())

timedict = dict(
    zip(["Z", "z", "Y", "y", "m", "d", "H", "M", "S", "p", "W", "j", "A", "B", "x", "X"],
        map(timestr, ["%Z", "%z", "%Y", "%y", "%m", "%d", "%H", "%M", "%S", "%p", "%W", "%j", "%A", "%B", "%x", "%X"])),
    week_cn=weekdict[timestr("%A")],
    month_cn=monthdict[timestr("%B")])

if __name__ == "__main__":
    pass