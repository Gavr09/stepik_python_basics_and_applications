import datetime
lst = input().split()
year, month, day = (int)(lst[0]), (int)(lst[1]), (int)(lst[2])
days = (int)(input())
date1 = datetime.date(year, month, day)
date2 = date1 + datetime.timedelta(days=days)
print(date2.year, date2.month, date2.day)
