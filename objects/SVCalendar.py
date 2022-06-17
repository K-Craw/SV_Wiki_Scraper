weekdayToDate = {
    'monday' : [1, 8, 15, 22],
    'tuesday' : [2, 9, 16, 23],
    'wednesday' : [3,10, 17, 24],
    'thursday' : [4, 11, 18, 25],
    'friday' : [5, 12, 19, 26],
    'saturday' : [6, 13, 20, 27],
    'sunday' : [7, 14, 21, 28]
    }

dateToWeekday = {
    [1, 8, 15, 22] : 'monday',
    [2, 9, 16, 23]: 'tuesday',
    [3, 10, 17, 24] : 'wednesday',
    [4, 11, 18, 25] : 'thursday',
    [5, 12, 19, 26] : 'friday',
    [6, 13, 20, 27] : 'saturday',
    [7, 14, 21, 28]: 'sunday'
    }

class SVCalendar:

    def getDayFromDate(date):
        for dates in dateToWeekday:
            if date in dates:
                return dateToWeekday[dates]

    def getDateFromDate(day):
        for weekday in weekdayToDate:
            if day == weekday:
                return weekdayToDate[day]