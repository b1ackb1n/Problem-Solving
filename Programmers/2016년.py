import datetime as dt
def solution(a, b):
    weeks = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    return weeks[dt.date(2016,a,b).weekday()]
