def is_leapyear(year,month,day):

    if (year%100)==0:
        if (year%400)==0:
            return True
        else:
            return False
    else:
        if (year%4)==0:
            return True
        else:
            return False

def days_for_month(year,month,day):
    if any([month==4,month==6,month==9,month==11]):
        return 30
    else:
        if month == 2:
            if (is_leapyear(year,month,day) == True):
                return 29
            else:
                return 28
        else:
            return 31

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < (days_for_month(year, month, day)):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

print (daysBetweenDates(2000,2,1,2013,3,1))
