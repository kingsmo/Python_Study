def solution(a, b):
    answer = ''
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    sum = 0
    for i in range(0, a-1):
        sum += month[i]
    sum += b-1
    answer = day[sum%7]

    return  answer
