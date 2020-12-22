from datetime import datetime, timedelta, date
from calendar import HTMLCalendar, monthrange

class Calendar(HTMLCalendar):
    # events will be a list of dictionaries each representing an event
    # the dictionary will have 3 keys: title, description, date
    
    def __init__(self, year=datetime.now().year, month=datetime.now().month, events=None):
        self.year = year
        self.month = month
        self.events = events
        super(Calendar, self).__init__()

    def displayMonth(self):
        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=True)}\n'
        cal += f'{self.formatweekheader()}\n'

        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.displayWeek(week)}\n'
        
        return cal

    def displayWeek(self, theweek):
        week = ''
        for d, weekday in theweek:
            week += self.displayDay(d)
        return f'<tr> {week} <tr>'

    def displayDay(self, theday):
        d = ''
        todays_events = [i for i in self.events if theday != 0 and datetime.strptime(i['date'], '%Y-%m-%d').date() == date(self.year, self.month, theday)]
        for event in todays_events:
            d += f'<li> ' + '<a href=\'' + event['description'] + '\'>' + event['title'] + '</a>' + ' </li>'

        if theday != 0:
            return f"<td><span class='date'>{theday}</span><ul> {d} </ul></td>"
        return '<td></td>'


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()
