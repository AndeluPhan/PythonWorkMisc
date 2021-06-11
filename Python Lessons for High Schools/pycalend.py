import calendar

print(calendar.weekheader(3))
print()

def intTODAY(day):
    if day == 0:
        print("Monday")
    elif day == 1:
        print("Tuesday")
    elif day == 2:
        print("Wednesday")
    elif day == 3:
        print("Thursday")
    elif day == 4:
        print("Friday")
    elif day == 5:
        print("Saturday")
    elif day == 6:
        print("Sunday")
    else:
        print("error")
print(calendar.firstweekday())
print()

print(calendar.month(2019,3,3))

print(calendar.monthcalendar(2019,3))

print(calendar.calendar(2019))

day_of_the_week = calendar.weekday(2020,6,7)
intTODAY(day_of_the_week)
print(calendar.isleap(2020))
print(calendar.leapdays(2000,2021))
