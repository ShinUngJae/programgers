import datetime

def solution(a, b) :
    day = datetime.date(2016, a, b)
    weekday_list = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    answer = weekday_list[day.weekday()]
    return answer


# 윤년
# 4의 배수의 년에는 2월 29일
# 단, 100의 배수인 년에는 2월 28일
# 단, 400의 배수이면 2월 29일

