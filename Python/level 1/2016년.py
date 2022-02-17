import datetime

def solution(a, b) :
    day = datetime.date(2016, a, b)
    weekday_list = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    answer = weekday_list[day.weekday()]
    return answer
